from loadData import loadData

from pyspark.sql import SparkSession
from pyspark.sql import types as type

spark = SparkSession.builder.master("local[*]").appName("ProjectRCP216").getOrCreate()

fields = [ type.StructField("var"+str(i), type.DoubleType(),True) for i in range(1,10001)]

schema = type.StructType(fields).add("label",type.StringType(),True)

loadDF = loadData(spark,schema)

#loadDF.dataShape()
#loadDF.printData()
#loadDF.printSchema()
