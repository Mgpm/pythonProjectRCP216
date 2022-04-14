
class preparationData: # pour la preparation des données
    def __init__(self,df,fn):
        self.df = df
        self.fn = fn

    def getDF(self):
        return self.df

    def printData(self):
        self.df.show(3, False)

    def printSchema(self):
        self.df.printSchema()

    def dataShape(self):
        print((self.df.count(), len(self.df.columns)))

    def dropDuplicates(self):
        self.df = self.df.dropDuplicates()


    def pourCentageMissingCols(self):
        missingCols = self.df
        missingCols = missingCols.select([(1 - (self.fn.count(c) / self.fn.count('*'))).alias(c + '_miss') for c in missingCols.columns])
        missingCols.select(missingCols.columns).distinct().show()

    def MissingImputed(self):
        multipliers = dict(self.df.select([(self.fn.mean(c)).alias(c) for c in self.df.columns]).collect()[0])
        self.df = self.df.fillna(multipliers)


    def addIdCol(self):
        self.df = self.df.select([self.fn.monotonically_increasing_id().alias('Id')] + [c for c in self.df.columns])

