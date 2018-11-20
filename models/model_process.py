import pandas as pd
from datetime import datetime
from data_transform import *
from classifier_train import *

num_feature_list = ['FRE_WT', 'FRE_APPT', 'LAT', 'LON', 'HOSP_LAT', 'HOSP_LON', 'HOSP_DIST', 'RECOMMEND_DT_TM_FLOAT', 'URGENCY_FLAG', 'URGENCY_CHG_IND']

cate_feature_list = ['GENDER', 'AGE','SUBURB', 'STATE', 'POSTCODE','LOC_FACILITY_CD_DISPLAY', 'PLANNED_PROCEDURE_DISPLAY','URGENCY_DISPLAY','WT_DUR_CATE']
       
    

def involk_training(input_feature_list,df):
    print('Training Random Forest...')
    X = df[input_feature_list]
    Y = df['WT_DUR_CATE_VEC']
    
    model = training_forest(X,Y)
    
    return model

def model_predict_output(model,input_feature_list,df):
    
    df['pred_value'] = model.predict(df[input_feature_list])
    
    res = model.predict_proba(df[input_feature_list])
    
    category = len(df['pred_value'].unique())
    
    keys = df.ENCNTR_ID
    
    for cate in range(category):
        key_prob = {}
        prob = res[:,cate]
        for i in range(len(keys)):
            key_prob[keys[i]] = prob[i]

        df[str(cate)] = df['ENCNTR_ID'].map(key_prob)
    
    
    df.to_csv('data/df_res.csv')
    
    
    
    
    
        
def main():
    
    df = pd.read_csv("data/patient_view/swslhd_comp_stat_no_doc_v2_3110.csv",dtype='unicode')
    
    values = {'HOSP_DIST': 9999,'STATE':'NA', 'LAT':0, 'LON': 0}
    
    df,vec_list = preprocess_data(df,10,values,cate_feature_list)
    vec_list.remove("WT_DUR_CATE_VEC")
    
    input_feature_list = vec_list + num_feature_list
    print('Training Random Forest...')
    clf_model = involk_training(input_feature_list,df)
    print('Produce Output...')
    # Export the model to a file
    time_now = str(datetime.utcnow().date())
    model_name = 'clf_rf_'+time_now+'.joblib'
    joblib.dump(clf_model, model_name)
    
    # Upload the model to GCS
#     bucket = storage.Client().bucket(BUCKET_NAME)
#     blob = bucket.blob('{}/{}'.format(
#     datetime.datetime.now().strftime('census_%Y%m%d_%H%M%S'),
#     model))
#     blob.upload_from_filename(model)

    
    
    model_predict_output(clf_model,input_feature_list,df)
    

if __name__ == '__main__':
    main()





