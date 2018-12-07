from __future__ import division
import math as m
import time
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]
input=[]
for i in range(100):
    a=random.randint(0, 10000000)
    b=random.randint(0, 10000000)
    l=[a,b]
    input.append(l)
k=5

def euclideanDist(a,b):
    result=m.sqrt(sum([m.pow((x-y),2) for x,y in zip(a,b)]))
    return result

class Cluster():
    def __init__(self):
        self.centroid=[]
        self.elements=[]

    def calculateCentroid(self):
        temp = [sum(x) for x in zip(*self.elements)]
      #  print zip(*self.elements)
        centroid = [x / (len(self.elements)) for x in temp]
        self.centroid = centroid

    def compactness(self, dist_fun=euclideanDist):
        c=0
        for x in self.elements: 
           # print("Vektor :" , x , " ", " Centroid: ", self.centroid)
            if(len(self.centroid)==0):
                print("Fail!")
            m=euclideanDist(x, self.centroid)
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
                distance=euclideanDist(x, self.clusters[i].centroid)
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
                        dist1=euclideanDist(d.centroid, t)
                        dist2=euclideanDist(c.centroid, t)
                        #print(x, "" , c.centroid ," " ,d.centroid, " ",t , " ", dist1, " ", dist2)
                        if dist1<dist2:
                           new=d
                    new.elements.append(t)
                    c.elements.remove(t)
                    new.calculateCentroid()
            clusterPlot(self.clusters)
        for i in range(k):
            self.clusters[i].calculateCentroid()

def clusterPlot(clusters):
    import matplotlib.pyplot as plot
    import numpy as np

    #fig = plot.figure()
    
    for c in clusters:
        elems = np.array(c.elements)
        plt.scatter(elems[:,0], elems[:,1])
        centroid = c.centroid
        plt.plot(centroid[0], centroid[1], 'X', c='black')
        fig.canvas.draw()
        time.sleep(1)

alg=kmeansClusterer()
alg.initializeCluster()
i=-1
plt.ion()
fig = plt.figure()
plt.show()
clusterPlot(alg.clusters)
alg.calculateCluster()
plt.show()
# # for i in range(k):
# #     print(alg.clusters[i].centroid, " ",alg.clusters[i].elements)
