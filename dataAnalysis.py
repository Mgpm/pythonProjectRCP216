
class dataAnalysis: #  Pour analyse descriptive et multidimensionnelle des données
    def __init__(self,plt,df):
        self.df = df
        self.plt = plt

    def getDF(self):
        return self.df


    def statsDescriptive(self):
        self.descriptive = self.df.describe([c for c in self.df.columns if c!="label"])
        self.descriptive.show()

    def correlation(self,spark):
        features = [c for c in self.df.columns if c!="label"]
        n_feature = len(features)
        corr = []
        for i in range(0,n_feature):
            temp = [None] * i
            for j in range(i,n_feature):
                temp.append(self.df.corr(features[i],features[j]))
            corr.append([features[i]] + temp)
        spark.createDataFrame(corr,['Column'] + features).show(5)


    def histoFunc(self,col):
        p = self.df.select(self.df[col]).collect()
        h = [i[0] for i in p]
        self.plt.hist(h,bins=10)


    def scatterFunc(self,col1,col2):
        p = self.df.select(self.df[col1],self.df[col2]).collect()
        c1 = [i[0][0] for i in p]
        c2 = [i[0][1] for i in p]
        self.plt.scatter(c1,c2,s=50,c='green')



    def scalerStandard(self, stVect, vectAss):
        self.scalerDF = stVect().setInputCol("features").setOutputCol('scalerfeatures')\
            .setWithStd(True)\
            .setWithMean(True)\
            .fit(vectAss)\
            .transform(vectAss)

    def vizData2D(self,pca):  # affiche le graphique 2D des données
        self.pcaDF = pca().setInputCol("scalerfeatures").setOutputCol("pcafeatures")\
        .setK(2).fit(self.scalerDF).transform(self.scalerDF).select("pcafeatures","label")   
        p = self.pcaDF.select(self.pcaDF["pcafeatures"]).collect()
        c1 = [i[0][0] for i in p]
        c2 = [i[0][1] for i in p]
        self.plt.scatter(c1,c2,s=50,c='green')
        
        
    def getPCA(self):
        return self.pcaDF
     



