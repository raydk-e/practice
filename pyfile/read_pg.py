import psycopg2
import pandas as pd

db_params = {
    "host": "localhost",
    "database": "analytics",
    "user": "learner",
    "password": "password"
}
table_name  = 'real_expense'

def read_table(table):
    try:
        con = psycopg2.connect(**db_params)
        cur = con.cursor()
        query = f"select * from {table};"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(row)
        df = pd.read_sql(query,con)
        print(df)
    except psycopg2.DatabaseError as e:
        print(f"database error  {e} ")
    except Exception as e:
        print(f"An unexpected error {e}")

    finally:
        if cur:
            cur.close()
        if con:
            con.close()
if __name__ == "__main__":
    read_table(table_name)



