import numpy as np
import pandas as pd
import datetime


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



def swv(t1_df,t2_df,hum_df) :
    
    """ input temperature data in factory , temperature data in coil , humidity data in factory 
        return saturated water vapor in coil temperature - water vapor in factory
    """

    loc_swv = t1_df.apply(lambda t1 : (6.11 * (10)**((7.5*t1)/(t1+237.3))) /10)
    coil_swv = t2_df.apply(lambda t2 :(6.11 * (10)**((7.5*t2)/(t2+237.3))) /10 )
    now_vr = (loc_swv*hum_df) / 100
    
    
    return coil_swv- now_vr



    return location
    

