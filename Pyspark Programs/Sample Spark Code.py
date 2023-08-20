from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample Spark Program").getOrCreate()
df = spark.read.csv("Learning/data/the_global_k_anon_dataset.csv", inferSchema=True, header=True)
df.select([ "Year", "Case_Category"]).show()