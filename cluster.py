
class cluster: # Pour la classification des données
    def __init__(self,k,plt,df):
        self.km=k
        self.plt = plt
        self.df = df

    def getDF(self):
        return self.df


    def clusterElbow(self,i,n):
        errors=[]
        for kn in range(i,n):
            kmean = self.km(k=kn,featuresCol="pcafeatures")
            model = kmean.fit(self.df)
            intra_distance = model.computeCost(self.df)
            errors.append(intra_distance)
        cluster_num = range(0,n)
        self.plt.figure(figsize=(15,5))
        self.plt.xlabel('Numbres de clusters')
        self.plt.ylabel('SSE')
        self.plt.plot(cluster_num,errors)

    
    def clusterPlot(self,n): # affiche le graphique des clusters
        kmean = self.km(k=n,featuresCol="pcafeatures",predictionCol="prediction",initMode="random")
        self.clusterDF = kmean.fit(self.df).transform(self.df)
        colors = ["blue","green","brown","red","yellow"]
        for i in range(0,n):
                p = self.clusterDF.filter(self.clusterDF["prediction"]==i).select(self.clusterDF["pcafeatures"]).collect()
                c1 = [col[0][0] for col in p]
                c2 = [col[0][1] for col in p]
                self.plt.scatter(c1,c2,s=50,c=colors[i])
        self.plt.show()
        
        
       
        
    def getCluster(self):
        self.clusterDF










