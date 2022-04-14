
from pyspark.ml.classification import RandomForestClassifier, DecisionTreeClassifier, GBTClassifier

class selectVar: # selection des features importances nous utilisé le cas RandomForestClassifier
    def __init__(self,df,pd,plt):
        self.df = df
        self.pd = pd
        self.plt = plt

    def getDF(self):
        return self.df

    def ModelByTreeDecision(self):
        self.model = DecisionTreeClassifier(featuresCol='features',labelCol='labelCode').fit(self.df)

    def ModelByGradienBooting(self):
        self.model = GBTClassifier(featuresCol='features',labelCol='labelCode').fit(self.df)

    def ModelByRandomForest(self):
        self.model = RandomForestClassifier(featuresCol='features',labelCol='labelCode').fit(self.df)

    def featureSelect(self): # determine les variables importantes par le model choisi
        self.featureImp = ["var"+str(i) for i in self.model.featureImportances.indices]
        self.featureImportances = self.pd.Series(index=self.featureImp, data=self.model.featureImportances.values)


    def featureSelectAllModel(self):
        m1 = DecisionTreeClassifier(featuresCol='features',labelCol='labelCode')
        m2 = GBTClassifier(featuresCol='features',labelCol='labelCode')
        m3 = RandomForestClassifier(featuresCol='features',labelCol='labelCode')
        dt1 = m1.fit(self.df)
        dt2 = m2.fit(self.df)
        dt3 = m3.fit(self.df)
        self.featureImp = ["var"+str(i) for i in dt1.featureImportances.indices]+["var"+str(i) for i in dt2.featureImportances.indices] + ["var"+str(i) for i in dt3.featureImportances.indices]+["label"]
        self.featureImp = list(set(self.featureImp))
        datas = dt1.featureImportances.values + dt2.featureImportances.values + dt3.featureImportances.values
        datas = list(set(datas))
        self.featureImportances = self.pd.Series(index=self.featureImp, data=datas)



    def plotFeatureImportances(self): # Affichage graphique des features Importances
        self.featureImportances.sort_values().plot(kind='barh',figsize=(5,50),title='Feature Importance')
        self.plt.show()

    def dataFeatureImportances(self): # Nouvelle dataframe après selection des variables selon leurs importances
        self.df = self.df.select(self.featureImp+["label"])




