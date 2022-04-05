
class loadData:
     def __init__(self, spark, sch):
          self.spark = spark
          self.sch = sch
          self.df = self.spark.read.format("csv").schema(self.sch).load('data.csv')

     def printData(self):
          self.df.show(3,False)

     def printSchema(self):
          self.df.printSchema()

     def dataShape(self):
          print((self.df.count(),len(self.df.columns)))