import psycopg2
import csv
import io

db_params ={
    'host': 'localhost',
    'database': 'analytics',
    'user': 'learner',
    'password': 'password'
}

table_name = 'real_expense'
csv_file_path = '/home/deepak/projects/practice/practice/final_clean.csv'

def csv_to_pgsql(csv_file, table):
    try:
        con = psycopg2.connect(**db_params)
        cur = con.cursor()
        with open (csv_file,'r', encoding='utf-8') as f:

            cur.copy_expert(
                 f"""
        COPY {table}
        FROM STDIN
        WITH (
            FORMAT CSV,
            HEADER TRUE,
            DELIMITER ',',
            NULL ''
        )
        """,f)
        con.commit()


        print("table is loaded")
    except(Exception, psycopg2.DatabaseError) as error:
        print(f" Error is {error}")

    finally:
        if cur:
            cur.close()
        if con:
            con.close()
if __name__ == '__main__':
    csv_to_pgsql(csv_file_path, table_name)

