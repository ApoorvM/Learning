from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample Spark Program").getOrCreate()
print(spark)