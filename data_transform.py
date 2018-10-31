'''
This is for transform categorical data to numerical(both level & non-level). 
'''
import pandas as pd


def set_dtype(df):
    time_col = ['RECOMMEND_DT_TM', 'LATEST_ACTIVE_STATUS_DT_TM'] 
    for col in time_col:
        df[col] = pd.to_datetime(df[col])

    df['WT_DUR'] = pd.to_timedelta(df['WT_DUR'])
    df['WT_DUR_DAYS'] = df['WT_DUR'].dt.days## grap days
    return df


def target_cate(df_attribute,num_bins):
    """
    transform to categorical attribute based on number of bins(percentile)
    Parameters
     ----------
    df_attribute : pandas serie (numerical)
     
    num_bins : int. Number of bins 

    Returns: pandas serie(categorical with Interval)
     -------
    """
    return pd.qcut(df_attribute, num_bins)


def transform_data(df,num_bins):
    df = set_dtype(df)
    df["WT_DUR_CATE"] = target_cate(df["WT_DUR_DAYS"],num_bins)
    
    
    return df
