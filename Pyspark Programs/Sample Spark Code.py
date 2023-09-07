from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample Spark Program").getOrCreate()
try:
    df = spark.read.csv("sample project/Learning/data/the_global_k_anon_dataset.csv", inferSchema=True, header=True)
    df.show()
except Exception as err:
    print(err)
