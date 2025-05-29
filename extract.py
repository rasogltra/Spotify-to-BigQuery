import pandas as pd
from dotenv import load_dotenv
import os
from google.cloud import bigquery

load_dotenv()

data= os.getenv("SPOTIFY_DATA")
project_id= os.getenv("PROJECT_ID")
dataset_id= os.getenv("DATASET_NAME")
table_name= os.getenv("TABLE_NAME")
 
def load_data_from_dataframe (dataframe, project_id, dataset_id, table_name):  
    try: 
        # Construct a BigQuery client object
        client = bigquery.Client()
        table_id=f"{project_id}.{dataset_id}.{table_name}"
 
        job_config = bigquery.LoadJobConfig(
            schema= [
            bigquery.SchemaField("rank", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("uri", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("artist_names", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("track_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("previous_rank", "INTEGER"),
            bigquery.SchemaField("weeks_on_chart", "INTEGER"),
            bigquery.SchemaField("streams", "INTEGER"),
            bigquery.SchemaField("load_at", "INTEGER", mode="REQUIRED")
                ]
            )

        job = client.load_table_from_dataframe (dataframe, table_id, job_config=job_config)
        job.result()
    
        table = client.get_table(table_id) # Make an API request
        print("Loaded {} rows and {} columns to {}".format (
            table.num_rows, len(table.schema), table_id
                )
            )
    except Exception as e:
        print(f"Unexpected error loading data to BigQuery: {e}")

if __name__ in '__main__':
    df = pd.read_csv(data)
    df['load_at'] = pd.Timestamp.utcnow()
    load_data_from_dataframe(df, project_id, dataset_id, table_name)
   