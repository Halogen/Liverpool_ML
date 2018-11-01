'''
This is for transform categorical data to numerical(both level & non-level). 
'''
import pandas as pd
from sklearn import preprocessing


def set_dtype(df):
    time_col = ['RECOMMEND_DT_TM', 'LATEST_ACTIVE_STATUS_DT_TM'] 
    for col in time_col:
        df[col] = pd.to_datetime(df[col])
        df[col+"_FLOAT"] = pd.to_timedelta(df[col]).dt.total_seconds().astype(int)
        


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


# def transform_data(df,num_bins):
#     df = set_dtype(df)
#     df["WT_DUR_CATE"] = target_cate(df["WT_DUR_DAYS"],num_bins)
    
    
#     return df

def cate_encode(df,cate_list):
    le = preprocessing.LabelEncoder()
    cate_to_num_features = []
    for feature in cate_list:
        vec_name = feature+"_VEC"
        cate_to_num_features.append(vec_name)
        df[vec_name] = le.fit_transform(df[feature])
        
    return df,cate_to_num_features
        

def preprocess_data(df,num_bins_target,values_fill_na,cate_list):
    
    df = set_dtype(df)
    df["WT_DUR_CATE"] = target_cate(df["WT_DUR_DAYS"],num_bins_target)
    ##fill nan according to given list
    df.fillna(value=values_fill_na,inplace=True)
    
    df,cate_feature_for_model = cate_encode(df,cate_list)
    
    return df,cate_feature_for_model
    
    
