# !pip install --upgrade google-cloud-bigquery[pandas,pyarrow]

from google.cloud import bigquery
import pandas as pd

class bquery_func:
    
    
    def __init__(self):
        """
        setup credential by a json file
        """
        self.client = bigquery.Client.from_service_account_json('credentials/LIVERPOOL DEMO-e778084b3d0f.json')
       
        
    def create_by_dataframe(self,df,dataset_id,table_id):
        '''
        add a new table from a pandas dataframe
        '''
        
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect=True
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_EMPTY ## write data only when table is empty
        
        
        dataset_ref = self.client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        self.client.load_table_from_dataframe(df, table_ref, location='US',job_config=job_config)
        
        
        
    def read_sql(self,sql):
        """
          read table by give a sql commend string
          return a dataframe
        """
        df = self.client.query(sql).to_dataframe()
        return df
    
    
    def append_table(self,df,dataset_id,table_id):
        """
        append dataframe to bigquery
        """
        
        dataset_ref = self.client.dataset(dataset_id)
        
        table_ref = dataset_ref.table(table_id)
        
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND ## apend the data
        
        self.client.load_table_from_dataframe(df, table_ref, location='US',job_config=job_config)
        
        
        return 
    