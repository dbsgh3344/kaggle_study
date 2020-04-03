import pandas as pd

def df_counting(p0_data,p1_data,x_data,variable_name):

    p0_df = pd.DataFrame(p0_data.game_id.value_counts().keys(),columns=['game_id'])
    p0_df.index = p0_df.game_id
    p0_df.drop('game_id',axis=1,inplace=True)

    p1_df = pd.DataFrame(p1_data.game_id.value_counts().keys(),columns=['game_id'])
    p1_df.index = p1_df.game_id
    p1_df.drop('game_id',axis=1,inplace=True)

    df = pd.DataFrame(x_data.game_id.unique(),columns=['game_id'])
    df.index = df.game_id
    df.drop('game_id',axis=1,inplace=True)

    p0_df['P0'+variable_name] = p0.game_id.value_counts().values
    p1_df['P1'+variable_name] = p1.game_id.value_counts().values

    df = pd.merge(df,p0_df,on='game_id',how='left')
    df = pd.merge(df,p1_df,on='game_id',how='left')

    df = df.fillna(0)

    x_data['P0'+variable_name] = df['P0'+variable_name]
    x_data['P1'+variable_name] = df['P1'+variable_name]
    x_data['delta'+variable_name] = x_data['P0'+variable_name] - x_data['P1'+variable_name]

    return x_data
