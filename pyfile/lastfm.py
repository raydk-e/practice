
from google.cloud import bigquery
import requests
from google.api_core.exceptions import NotFound

PROJECT_ID = "raydeepak0206"
DATASET = "dataexp"
TABLE_ID = "lastfm_tag"
client =  bigquery.Client(project=PROJECT_ID)



full_table = f"{PROJECT_ID}.{DATASET}.{TABLE_ID}"

def create_table_if_not_exist():
    try:
        client.get_table(full_table)
        print("table already exist")
    except NotFound:

        schema = [
            bigquery.SchemaField("name", "STRING", mode= "NULLABLE"),
            bigquery.SchemaField("url", "STRING", mode= "NULLABLE"),
            bigquery.SchemaField("count", "INTEGER", mode= "NULLABLE")
        ]
        table = bigquery.Table(full_table,schema=schema)
        client.create_table(table=table)
        print(f"Created table")


def  fetch_lastfm():
    url = "http://ws.audioscrobbler.com/2.0/"
    payload = {
        "method" : "album.gettoptags",
        "artist" : "radiohead",
        "album" : "the bends",
        "api_key" : "b4438a97b63514aec6a46c3d7be18673",
        "format" : "json"
        }
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()

        data = response.json()
        # print(data)
        tags = data.get('toptags',{}).get('tag',[])
        print(tags)

        for tag in tags:
            if 'count' in tag:
                try:
                    tag['count'] = int(tag['count'])
                except(ValueError, TypeError):
                    tag['count'] = 0
        return tags
    except requests.exceptions.RequestException as e:
        print(f"Error While Reading the API : {e}")

create_table_if_not_exist()
rows_to_insert = fetch_lastfm()

if rows_to_insert:
    job_config = bigquery.LoadJobConfig(
        write_disposition = "WRITE_APPEND",
    )
    load_job = client.load_table_from_json(
        rows_to_insert,
        full_table,
        job_config=job_config

    )
    print("Starting load job")
    load_job.result()
    print(f"Successful load {len(rows_to_insert)} rows inserted")
else:
    print("No data to insert")
