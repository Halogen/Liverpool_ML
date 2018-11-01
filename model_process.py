import pandas as pd
from data_transform import *
from classifier_train import *

   
    

def involk_process(input_feature_list,df):
    train,test = 
    
    
    
    
    
    
    
def main():
    num_feature_list = ['FRE_WT', 'FRE_APPT', 'LAT', 'LON', 'HOSP_LAT', 'HOSP_LON', 'HOSP_DIST', 'RECOMMEND_DT_TM', 'LATEST_ACTIVE_STATUS_DT_TM', 'URGENCY_FLAG', 'URGENCY_CHG_IND']
    cate_feature_list = ['GENDER', 'AGE','SUBURB', 'STATE', 'POSTCODE','LOC_FACILITY_CD_DISPLAY', 'PLANNED_PROCEDURE_DISPLAY','URGENCY_DISPLAY']
    
    df = pd.read_csv("",dtype='unicode')
    
    values = {'HOSP_DIST': 9999,'STATE':'NA', 'LAT':0, 'LON': 0}
    
    df = preprocess_data(df,10,values,cate_feature_list)
    
    
    dt = process_data_pd()
    pos_data, neg_data = text2vec()
    print('Running SMOTE... to rebalance')
    new_pos_data = gen_data_set_with_smote(pos_data)
    print('New positive data size:', new_pos_data.shape[0])
    data = np.concatenate((new_pos_data, neg_data))
    label = ['1']*new_pos_data.shape[0] + ['0']*neg_data.shape[0]
    
    
    print('Training Random Forest...')
    model = training_forest(data, label)

    test_data = np.concatenate((pos_data, neg_data))
    test_forest(model, test_data)
    print('Write result to file...')
    output_res_new(dt)


if __name__ == '__main__':
    main()





