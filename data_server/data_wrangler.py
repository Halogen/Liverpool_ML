import pandas as pd
import numpy as np

class data_wrangler:
    

    def __init__(self,df):
        self.numeric_col = df._get_numeric_data().columns
        self.object_col = [x for x in df.columns if x not in self.numeric_col]
        self.df = df.copy()
        

    def str_with_na(self,row):
        if pd.isna(row):
            return np.nan
        else:
            return str(int(row))


    def edit_dtype(self):
        for col in self.numeric_col:
            if col != 'AGE':
                if pd.isnull(self.df[col]).any():
                    self.df[col] = self.df[col].apply(lambda row: self.str_with_na(row))
    #                 print('change1')
                else:
                    self.df[col] = self.df[col].astype(str)
    #                 print('change2')
        for col in self.object_col:
            self.df[col] = self.df[col].apply(lambda row: np.nan if row ==' ' else row)
#             print('change3')
        return self.df

    def edit_timestamp(self,df):
#         if df==None:
#             df=self.df.copy()            
#         else:
#             df=df.copy()
        for col in df.columns:
            if col.find('DT_TM')>=0:
                df[col]=pd.to_datetime(df[col])
                print(col)
        return df
    
    

        
    def data_separate(self,df):
        '''
        separate data to different components
        for safety reason instead of using list of column name
        use index 
        '''
        saperator = ['PATIENT_DATA',  'WAITLIST_DATA', 'WAITLIST_HIST_DATA', 'ENCOUNTER_DATA', 'APPOINTMENT_DATA', 'SURGICAL_CASE_DATA', 'SURGICAL_CASE_ATTENDEE_DATA']
        
        saperator_num = []
        for s in saperator:
            saperator_num.append(list(df.columns).index(s))
            
        
        patient_col = list(df.columns[(saperator_num[0]+1):saperator_num[1]])
        patient_col.append('ENCNTR_ID')
        
        wl_col = list(df.columns[(saperator_num[1]+1):saperator_num[2]])
        wl_col.append('ENCNTR_ID')
        
        wlh_col = list(df.columns[(saperator_num[2]+1):saperator_num[3]])
        wlh_col.append('ENCNTR_ID')
        
        encntr_col = list(df.columns[(saperator_num[3]+1):saperator_num[4]])
        ap_col = list(df.columns[(saperator_num[4]+1):saperator_num[5]])
        sc_col = list(df.columns[(saperator_num[5]+1):saperator_num[6]])
        sca_col = list(df.columns[(saperator_num[6]+1):])
        
        df_dic = {}
        df_dic['PATIENT_DATA'] = df[patient_col].drop_duplicates()
        df_dic['WAITLIST_DATA'] = df[wl_col].drop_duplicates()
        df_dic['WAITLIST_HIST_DATA'] = df[wlh_col].drop_duplicates()
        df_dic['ENCOUNTER_DATA'] = df[encntr_col].drop_duplicates()
        df_dic['APPOINTMENT_DATA'] = df[ap_col].drop_duplicates()
        df_dic['SURGICAL_CASE_DATA'] = df[sc_col].drop_duplicates()
        df_dic['SURGICAL_CASE_ATTENDEE_DATA'] = df[sca_col].drop_duplicates()
        
        
        return df_dic
        
        
   
    def pipeline1(self):
        '''
        rules to follow
        BEG_EFFECTIVE_DT_TM  == BEG_EFFECTIVE_DT_TM_2
        BEG_EFFECTIVE_DT_TM_1 == BEG_EFFECTIVE_DT_TM_2
        '''
#         if df==None: df = self.df

        self.df = self.edit_dtype()
        self.df = self.edit_timestamp(self.df)
        
        df1 = self.df[abs(self.df.BEG_EFFECTIVE_DT_TM-self.df.BEG_EFFECTIVE_DT_TM_2)<pd.to_timedelta('1 days')].copy()
        df2 = df1[abs(df1.BEG_EFFECTIVE_DT_TM_1-df1.BEG_EFFECTIVE_DT_TM_2)<pd.to_timedelta('1 days')].copy()
        
        df2_dict = self.data_separate(df2)
        
        return df2,df2_dict    
    

    
        
        
        
