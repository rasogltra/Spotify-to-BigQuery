# BigQuery ETL Pipline - Music Streaming Analytics

This project demonstrates an end-to-end ETL using Python and Google BigQuery. The pipeline pulls Spotify music data (eg. Top Global Songs Daily) from a downloadable public `.csv` file, here: https://spotifycharts.com/regional/global/daily/latest, processes it using pandas and loads it into a BigQiery dataset.

## Requirements
- Python 3.12.1
- pandas
- Google BigQuery 
- Google Cloud account
- `.csv` dataset (from Spotify or Kaggle)

## How it works
1. **Extract**: Pulls song data from Spotify CSV dataset.
2. **Transform**: Standardizes the data (e.g, timestamp formatting).
3. **Load**: Uploads the processed data to a specified BigQuery table.

### OPTINAL: Create a Virtual Environment for code and dependencies

### Install dependencies
```pip install -r requirements.txt```

### Set environment variables
1. Export your Spotify and GCLoud credentials in bash or you can create a `.env` file and modify `extract.py` to accept the variables.
```export SPOTIFY_CLIENT_ID=your_client_id```

```export SPOTIFY_CLIENT_SECRET=your_client_secret```

```export GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json```

3. Create a `.env` file and add BiqQuery table/data details.
```PROJECT_ID= "your-goolge_cloud-project-id"```

```DATASET_NAME="your_dataset-id"```

```TABLE_NAME="your-table-name"```

### Run the ETL
`python extract.py`

### Upcoming Enhancements
- Schedule the ETL with Airflow
- Add more data sources (e.g. Spotify API)
