import pandas as pd
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql import functions as fn
from pyspark.sql import types as type
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler,StringIndexer,PCA,StandardScaler

from loadData import loadData
from preparationData import preparationData
from selectVar import selectVar
from dataAnalysis import dataAnalysis
from vAssembler import vAssembler
from cluster import cluster

spark = SparkSession.builder.master("local[*]").appName("ProjectRCP216").getOrCreate()

fields = [ type.StructField("var"+str(i), type.DoubleType(),True) for i in range(0,10000)]

schema = type.StructType(fields).add("label",type.StringType(),True)

loadDF = loadData(spark,schema,fn)



