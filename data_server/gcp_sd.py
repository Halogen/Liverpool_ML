# !pip install --upgrade google-cloud-bigquery[pandas,pyarrow]

from google.cloud import bigquery
import pandas as pd
import io

from google.cloud import storage


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
    
    
class gcp_storage:
    
    def __init__(self,bucket_id):
        """
        setup credential by a json file
        """
        self.client = storage.Client.from_service_account_json('credentials/LIVERPOOL DEMO-e778084b3d0f.json')
        self.bucket = self.client.get_bucket(bucket_id)
        
    def read_to_str(self,path):
        
        blob = self.bucket.blob(path)
        
        return blob.download_as_string()
        
    def read_csv(self,path):
        
        iofile = self.read_to_str(path)
        df = pd.read_csv(io.BytesIO(iofile),low_memory=False)
        
        return df
        
    def upload_file_string(self, file_stream, path_filename, content_type):
        """
        Uploads a string to a given Cloud Storage bucket and returns the public url
        to the new object.
        """
        #fow_logger.info('filename ' + str(filename) + " b " + str(bucket_name))
        blob = bucket.blob(path_filename)

        #fow_logger.info("uploading file " + str(filename) + " into " + str(bucket_name))
        blob.upload_from_string(
            file_stream,
            content_type=content_type)
#         fow_logger.info("Uploaded input files into " + str(bucket_name))
        
        return blob
    
    def upload_file(self, file, path_filename, content_type):
        """
        Uploads a file object.
        example: open('file.py') as file: upload_file
        
        """
        #fow_logger.info('filename ' + str(filename) + " b " + str(bucket_name))
        blob = bucket.blob(path_filename)

        #fow_logger.info("uploading file " + str(filename) + " into " + str(bucket_name))
        blob.upload_from_file(
            file,
            content_type=content_type)
#         fow_logger.info("Uploaded input files into " + str(bucket_name))
        
        return blob
    
    def upload_filename(self, filename, path_filename):
        """
        Uploads a filename (path where the file is in logal env)
        """
        #fow_logger.info('filename ' + str(filename) + " b " + str(bucket_name))
        blob = bucket.blob(path_filename)

        #fow_logger.info("uploading file " + str(filename) + " into " + str(bucket_name))
        blob.upload_from_filename('temp_folder/'+filename)
#         fow_logger.info("Uploaded input files into " + str(bucket_name))
        
        return blob
    
    
    def upload_df_csv(self,df,filename,path):
        """
        upload pandas dataframe to storage as a CSV file
        """
        df.to_csv('temp_dir/'+filename)# create file 
        path_filename = path+'/'+filename# for blob
        
        self.upload_filename('temp_dir/'+filename, path_filename)
        os.remove('temp_dir/'+filename)# delete file after upload
        
        return 
        
        
      
    def upload_model_joblib(self,model,filename,path):
       
        joblib.dump(model, 'temp_dir/'+filename)# create file 
        path_filename = path+'/'+filename

        self.upload_filename('temp_dir/'+filename, path_filename)
        os.remove('temp_dir/'+filename)# delete file after upload
        
        return 
          