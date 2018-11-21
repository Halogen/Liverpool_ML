import pandas as pd

class feature_eng:
    
    def __init__(self):
        
        return
    
    def geo_latlon(self,df):
        
        df_oversea = df[df['SUBURB'] == 'OVERSEAS'].copy()
        df_oversea['LAT'] = 90        
        df_oversea['LON'] = 60
        df_nofix = df[df['SUBURB'] == 'NO FIXED ADDRESS'].copy()
        df_nofix['LAT'] = 0
        df_nofix['LON'] = 0
        
        
        df_special = df[df['POSTCODE'] == '2164no'].copy()
        df_special['POSTCODE'] = '2164'
        df_norm = df[(df['SUBURB'] != 'NO FIXED ADDRESS') & (df['SUBURB'] != 'OVERSEAS') & (df['POSTCODE'] != '2164no')]
        df_norm = pd.concat([df_norm,df_special],axis=0)
        
        au_geo = pd.read_csv("static_data/Australian_Post_Codes_Lat_Lon.csv")[['postcode','suburb','lat','lon']]
        au_geo.columns = ['POSTCODE','SUBURB','LAT','LON']
        au_geo['POSTCODE']=au_geo['POSTCODE'].astype(str)
        au_geo_1 = au_geo[['POSTCODE','LAT','LON']].copy()
        au_geo_2 = au_geo[['SUBURB','LAT','LON']].copy()
        
        
        df_geo_norm = pd.merge(df_norm, au_geo, how='left', on=['POSTCODE','SUBURB'])
        
        df_geo_norm_1 = df_geo_norm[pd.notnull(df_geo_norm.LAT)].copy()
        
        df_geo_norm_2 = df_geo_norm[pd.isnull(df_geo_norm.LAT)][df_norm.columns].copy()           
        df_geo_norm_2 = pd.merge(df_geo_norm_2, au_geo_1, how='left', on=['POSTCODE'])
        
        df_geo_norm_3 = df_geo_norm_2[pd.isnull(df_geo_norm_2.LAT)][df_norm.columns].copy()
        df_geo_norm_2 = df_geo_norm_2[pd.notnull(df_geo_norm_2.LAT)]
        
        df_geo_norm_3 = pd.merge(df_geo_norm_3, au_geo_2, how='left', on=['SUBURB'])
        
        
        df_geo = pd.concat([df_geo_norm_1,df_geo_norm_2,df_geo_norm_3,df_oversea,df_nofix],axis=0)
        
        df_geo_result = df_geo.dropna()
        
        return df_geo_result
    
    
    
    
    
        
        





