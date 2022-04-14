
class loadData:
     def __init__(self, spark, sch,fn):
          self.spark = spark
          self.sch = sch
          self.fn = fn
          self.df = self.spark.read.format("csv").schema(self.sch).load('data.csv')

     def getDF(self):
          return self.df









































