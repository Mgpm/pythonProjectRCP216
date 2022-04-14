

class vAssembler: # vectorise le dataframe
    def __init__(self,fn,df):
        self.df = df
        self.fn = fn

    def getDF(self):
        return self.df

    def vectStringIndex(self,stringIndexer):
        str = stringIndexer().setInputCol("label").setOutputCol("labelCode")
        self.df = str.fit(self.df).transform(self.df)

    def vectAssembler(self,vectorAssembler):

        vectAss = vectorAssembler().setInputCols(self.df.columns[:-2]).setOutputCol('features')
        self.df = vectAss.transform(self.df)