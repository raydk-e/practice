import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

SERVICE_ACCOUNT_FILE = 'keys/creds.json'

def get_gsheet_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    cred = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE,scope)
    client = gspread.authorize(cred)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1bcP8nTYLpxW7RsM3oCd5DyqjWF8EFkpvLWHXMe2YVzE/edit?pli=1&gid=0#gid=0").sheet1
    return sheet.get_all_records()

def run():
    project_id = 'raydeepak0206'
    dataset = 'dataexp'
    table_name = 'books'
    destination_table = f"{project_id}.{dataset}.{table_name}"


    options = PipelineOptions(
        flags =  [],
        project = project_id,
        runner = 'DirectRunner'
    )

    with beam.Pipeline(options = options) as p:
        (
            p
            |"Read from sheet" >> beam.Create(get_gsheet_data())
            |"Write to Bigquery" >> beam.io.WriteToBigQuery(
                destination_table,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                # method="STREAMING_INSERTS"
                method="FILE_LOADS"
                )
        )
    print(f"Success! Data loaded to {destination_table}")

if __name__ == "__main__":
    run()










