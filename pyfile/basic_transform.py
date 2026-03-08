from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, when

spark = SparkSession.builder\
        .appName("basic_transform")\
        .getOrCreate()

try:
    df = spark.read\
        .options("header" , "true")\
        .options("inferSchema", "true")\
        .csv("mnt/c/D/01Deepak/02SelfStudy/SparkLearning/books_dataset.csv")    
    print(df.schema)

    df.show()
except Exception as e:
    print(f"Error Occurred {e}")

finally:
    spark.stop()