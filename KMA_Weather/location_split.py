import pandas as pd


def loc_split(data,plant_num):
    """split plant data by location
    input data, plant number
    output data splited by location number 
    """

    plant_num = str(plant_num)
    data['plant'+plant_num+'_train.mea_ddhr'] = pd.to_datetime((data['plant'+plant_num+'_train.mea_ddhr']))
    
    loc1 = data[['plant'+plant_num+'_train.mea_ddhr', 'plant'+plant_num+'_train.tem_in_loc1',
       'plant'+plant_num+'_train.hum_in_loc1', 'plant'+plant_num+'_train.tem_coil_loc1',
       'plant'+plant_num+'_train.tem_out_loc1', 'plant'+plant_num+'_train.hum_out_loc1','plant'+plant_num+'_train.cond_loc1']]
    
    loc2 = data[['plant'+plant_num+'_train.mea_ddhr','plant'+plant_num+'_train.tem_in_loc2', 'plant'+plant_num+'_train.hum_in_loc2',
       'plant'+plant_num+'_train.tem_coil_loc2','plant'+plant_num+'_train.tem_out_loc1', 'plant'+plant_num+'_train.hum_out_loc1',
        'plant'+plant_num+'_train.cond_loc2',]]

    loc3 = data[['plant'+plant_num+'_train.mea_ddhr','plant'+plant_num+'_train.tem_in_loc3','plant'+plant_num+'_train.hum_in_loc3', 
                 'plant'+plant_num+'_train.tem_coil_loc3','plant'+plant_num+'_train.tem_out_loc1',
                 'plant'+plant_num+'_train.hum_out_loc1','plant'+plant_num+'_train.cond_loc3',]]

    return loc1,loc2,loc3
    