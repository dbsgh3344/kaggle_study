import numpy as np
import pandas as pd
import datetime
from sklearn.preprocessing import StandardScaler,MinMaxScaler

def loc_func(location,plant_num,loc_num):
    """ input location data, plant number, location number 
	return location DataFrame"""


    plant_num = str(plant_num)
    loc_num = str(loc_num)



    # 24h �� date column ����
    location['24h_datetime']  =location['datetime'] + datetime.timedelta(hours=24)
    
    # 48h �� date column ����
    location['48h_datetime']  =location['datetime'] + datetime.timedelta(hours=48)

    cond_lists24 = []
    cond_lists48 = []
    
    for i in range(len(location)):
        # try :
            # print( loc1.loc[loc1['datetime']==i,'plant1_train.cond_loc1'].notnull().bool())
        if location.loc[location['datetime']== location['24h_datetime'][i],'plant'+plant_num+'_train.cond_loc'+loc_num].notnull().any():
            cond_lists24.append(location.loc[location['datetime']==location['24h_datetime'][i],'plant'+plant_num+'_train.cond_loc'+loc_num].item())
        else: 
            cond_lists24.append(-1)

        if location.loc[location['datetime']== location['48h_datetime'][i],'plant'+plant_num+'_train.cond_loc'+loc_num].notnull().any():
            cond_lists48.append(location.loc[location['datetime']==location['48h_datetime'][i],'plant'+plant_num+'_train.cond_loc'+loc_num].item())
        else: 
            cond_lists48.append(-1)

        # except :
            # print(loc1.loc[loc1['datetime']==i,'plant1_train.cond_loc1'].item())    
    location['24h_cond'] = cond_lists24
    location['48h_cond'] = cond_lists48

    return location


def swv(t1_df,t2_df,hum_df) :
    
    """ input temperature data in factory , temperature data in coil , humidity data in factory 
        return saturated water vapor in coil temperature - water vapor in factory
    """

    loc_swv = t1_df.apply(lambda t1 : (6.11 * (10)**((7.5*t1)/(t1+237.3))) /10)
    coil_swv = t2_df.apply(lambda t2 :(6.11 * (10)**((7.5*t2)/(t2+237.3))) /10 )
    now_vr = (loc_swv*hum_df) / 100
    
    
    return coil_swv- now_vr



    
    




def resampling_scaling(df, resm_period,sc_col_st,sc_col_end, ):
    """ input 
        dataframe,  
        resampling perioid (str) : pandas resampling method,  
        scaling column start number (int): will use sliding   
        scaling column end number (int): will use sliding  
        """
    
    df_h= df.resample(resm_period).mean()
    df_h = df_h.interpolate()
    
    mms = MinMaxScaler()

    mms.fit(df_h.iloc[:,sc_col_st:sc_col_end])
    scaled_x = mms.transform(df_h.iloc[:,sc_col_st:sc_col_end])
    
    df= pd.DataFrame(scaled_x)

    return df


def create_squence(x,time_steps,col_st,col_end):
    """input dataframe, time step (int),  
    col_st : to sequence col start number    
     col_end : to sequence col end number  
      
    output 3d array x_train, 2d array y_train  
    """



    
    x_list =[]
    y_list =[]
    for i in range(len(x)-time_steps):
        sequence = x.iloc[i:i+time_steps,col_st:col_end].values
        label =x.iloc[i+time_steps,col_st:col_end].values
        
        x_list.append(sequence)
        y_list.append(label)
    
    return np.array(x_list),np.array(y_list)  



def create_test_sequence(x,dates):
    """ input dataframe  
        dates (str) : ex) 1 days , 2 days     
        will use all column   
        not available time step so, will use datetime index to make 24h, 48h time series data  
	  
	output 3d array x_test  

    """


    test_x = []
    for i in range(len(x)):
        day= x.index[i] +pd.Timedelta(dates)
        # twoday= x.index[i] +pd.Timedelta('2 days')
        
        val = x.loc[x.index[i]:day].values

        
# [[ 'plant_test.hum_in','plant_test.tem_in','plant_test.tem_coil','plant_test.tem_out_loc1','plant_test.hum_out_loc1']]
        test_x.append(val)

    return np.array(test_x)

