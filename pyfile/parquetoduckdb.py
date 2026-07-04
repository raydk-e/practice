import os
import duckdb
import pandas as pd

DB_PATH = "local_datalake.db"

print(f" connecting to duckdb datalake file: {DB_PATH}")

con =  duckdb.connect(DB_PATH)

print("\n--------------Processing Bronze layer-------------------")

con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")

file_path = os.path.join("/home/deepak/projects/practice/practice/datafile/", "*.parquet")

con.execute (f"""CREATE TABLE IF NOT EXISTS bronze.raw_sales AS
             SELECT * FROM read_parquet('{file_path}');
             """)

print("\-----------------Processing Silver Layer----------------")
con.execute("CREATE SCHEMA IF NOT EXISTS silver;")

con.execute("""
            CREATE OR REPLACE TABLE silver.agg_sales AS
            SELECT product_name,
            product_id,
            COUNT(product_id) AS item_count,
            product_category,
            SUM(mrp) AS sales_sum,
            SUM(sell_price) As sell_price_sum,
            transaction_date
            FROM bronze.raw_sales

            GROUP BY
            product_id, transaction_date, product_name, product_category
            """

             )

print("\----------------- Silver Layer Created----------------")

print("\n----data lake verification----")

print("show all tables")

con.sql("SHOW ALL TABLES;").show()

print("\n sample data from bronze layer")

print(con.sql("SELECT * FROM bronze.raw_sales LIMIT 10;").df())
print(con.sql("SELECT * FROM silver.agg_sales LIMIT 10;").df())

con.close()

print("pipeline completes")
