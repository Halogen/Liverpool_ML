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

    def edit_timestamp(self):
        

# df["PM_WAIT_LIST_ID"] = df["PM_WAIT_LIST_ID"].apply(lambda row: str_with_na(row))
# df["ACTIVE_IND"] = df["ACTIVE_IND"].apply(lambda row: str_with_na(row))
# df["PM_WAIT_LIST_HIST_ID"] = df["PM_WAIT_LIST_HIST_ID"].apply(lambda row: str_with_na(row))
# df["ACTIVE_IND_1"] = df["ACTIVE_IND_1"].apply(lambda row: str_with_na(row))
# df["SCH_APPT_ID"] = df["SCH_APPT_ID"].apply(lambda row: str_with_na(row))
# df["SCHEDULE_ID"] = df["SCHEDULE_ID"].apply(lambda row: str_with_na(row))
# df["BOOKING_ID"] = df["BOOKING_ID"].apply(lambda row: str_with_na(row))
# df["SCH_EVENT_ID"] = df["SCH_EVENT_ID"].apply(lambda row: str_with_na(row))
# df["CA_CASE_ATTENDANCE_ID"] = df["CA_CASE_ATTENDANCE_ID"].apply(lambda row: str_with_na(row))
# df["CA_ACTIVE_IND"] = df["CA_ACTIVE_IND"].apply(lambda row: str_with_na(row))
# df["CA_SURG_CASE_ID"] = df["CA_SURG_CASE_ID"].apply(lambda row: str_with_na(row))
# df["SC_SURG_CASE_ID"] = df["SC_SURG_CASE_ID"].apply(lambda row: str_with_na(row))
# df["SC_SCH_EVENT_ID"] = df["SC_SCH_EVENT_ID"].apply(lambda row: str_with_na(row))
# df["SA_ENCNTR_ID"] = df["SA_ENCNTR_ID"].apply(lambda row: str_with_na(row))


# df["STATE"] = df["STATE"].apply(lambda row: np.nan if row ==' ' else row)

# df["PLANNED_PROCEDURE_DISPLAY"] = df["PLANNED_PROCEDURE_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["PLANNED_PROCEDURE_DISPLAY"] = df["PLANNED_PROCEDURE_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["REASON_FOR_CHANGE_DISPLAY"] = df["REASON_FOR_CHANGE_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["REASON_FOR_REMOVAL_DISPLAY"] = df["REASON_FOR_REMOVAL_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["URGENCY_DISPLAY"] = df["URGENCY_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["PLANNED_PROCEDURE_DISPLAY_HST"] = df["PLANNED_PROCEDURE_DISPLAY_HST"].apply(lambda row: np.nan if row ==' ' else row)
# df["REASON_FOR_CHANGE_DISPLAY_HST"] = df["REASON_FOR_CHANGE_DISPLAY_HST"].apply(lambda row: np.nan if row ==' ' else row)
# df["REASON_FOR_REMOVAL_DISPLAY_HST"] = df["REASON_FOR_REMOVAL_DISPLAY_HST"].apply(lambda row: np.nan if row ==' ' else row)
# df["URGENCY_DISPLAY_HST"] = df["URGENCY_DISPLAY_HST"].apply(lambda row: np.nan if row ==' ' else row)
# df["LOC_NURSE_UNIT_CD_DISPLAY"] = df["LOC_NURSE_UNIT_CD_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["LOC_TEMP_CD_DISPLAY"] = df["LOC_TEMP_CD_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["ACTIVE_STATUS_CD_DISPLAY"] = df["ACTIVE_STATUS_CD_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["PROC_ROOM"] = df["PROC_ROOM"].apply(lambda row: np.nan if row ==' ' else row)
# df["CANCEL_REASON_DISPLAY"] = df["CANCEL_REASON_DISPLAY"].apply(lambda row: np.nan if row ==' ' else row)
# df["CLINICIAN_ROLE"] = df["CLINICIAN_ROLE"].apply(lambda row: np.nan if row ==' ' else row)
# df["CLINICIAN"] = df["CLINICIAN"].apply(lambda row: np.nan if row ==' ' else row)



    
    
# df["PERSON_ID"] = df["PERSON_ID"].astype(str)
# df["MRN"] = df["MRN"].astype(str)
# df["CMRN"] = df["CMRN"].astype(str)
# df["ENCNTR_ID"] = df["ENCNTR_ID"].astype(str)
# df["ORGANIZATION_ID"] = df["ORGANIZATION_ID"].astype(str)
# df["ACTIVE_IND_2"] = df["ACTIVE_IND_2"].astype(str)


