
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EcommerceDataProcessing") \
    .getOrCreate()

df = spark.read.format("jdbc").options(
    url="jdbc:postgresql://postgres:5432/orders_db",
    dbtable="orders",
    user="postgres",
    password="password"
).load()

# Perform some aggregation or analysis
df.groupBy("customer_id").count().show()

spark.stop()
