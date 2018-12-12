from __future__ import division
import random
import matplotlib.pyplot as plt
import distFunctions as dist
import plotFunctions as plots

#input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]
input=[]
for i in range(100):
    a=random.randint(0, 10000000)
    b=random.randint(0, 10000000)
    l=[a,b]
    input.append(l)
k=5

class Cluster():
    def __init__(self):
        self.centroid=[]
        self.elements=[]

    def calculateCentroid(self):
        temp = [sum(x) for x in zip(*self.elements)]
      #  print zip(*self.elements)
        centroid = [x / (len(self.elements)) for x in temp]
        self.centroid = centroid

    def compactness(self, dist_fun=dist.euclideanDist):
        c=0
        for x in self.elements: 
           # print("Vektor :" , x , " ", " Centroid: ", self.centroid)
            if(len(self.centroid)==0):
                print("Fail!")
            m=dist.euclideanDist(x, self.centroid)
            m=m*m
            c=c+m
        return c    
    
class kmeansClusterer():

    def __init__(self):
        self.clusters=[]

    def initializeCluster(self):
        for i in range(k):
            self.clusters.append(Cluster())
            self.clusters[i].centroid=input[i]
        for x in input:
            pre=-1
            c=None
            for i in range(k):
                distance=dist.euclideanDist(x, self.clusters[i].centroid)
                if(pre==-1):
                    #first loop
                    pre=distance
                    c=i
                else:
                    if distance < pre:
                        c=i
                        pre=distance
            self.clusters[c].elements.append(x)
        for i in range(k):
            self.clusters[i].calculateCentroid()

    def calculateCluster(self):
        for x in range(10):
            for c in self.clusters:
                for t in c.elements:
                    new=c
                    for d in self.clusters:
                        dist1=dist.euclideanDist(d.centroid, t)
                        dist2=dist.euclideanDist(c.centroid, t)
                        #print(x, "" , c.centroid ," " ,d.centroid, " ",t , " ", dist1, " ", dist2)
                        if dist1<dist2:
                           new=d
                    new.elements.append(t)
                    c.elements.remove(t)
                    new.calculateCentroid()
            clusterPlot(self.clusters)
        for i in range(k):
            self.clusters[i].calculateCentroid()



alg=kmeansClusterer()
alg.initializeCluster()
fig = plt.figure()
plots.listClusterPlot(alg.clusters)
