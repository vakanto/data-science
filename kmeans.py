from __future__ import division
import math as m

input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7]]
k=3


class Cluster():
    def __init__(self):
        self.centroid=[]
        self.elements=[]

    def calculateCentroid(self):
        temp = [sum(x) for x in zip(*self.elements)]
        print zip(*self.elements)
        centroid = [x / (len(self.elements)) for x in temp]
        self.centroid = centroid
    

def euclideanDist(a,b):
    result=m.sqrt(sum([m.pow((x-y),2) for x,y in zip(a,b)]))
    #print result
    #print result
    return result

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
        for x in range(5):
            for c in self.clusters:
                for t in c.elements:
                    for d in self.clusters:
                        dist1=euclideanDist(d.centroid, t)
                        dist2=euclideanDist(c.centroid, t)

                        print(x, "" , c.centroid ," " ,d.centroid, " ",t , " ", dist1, " ", dist2)
                        if dist1<dist2:
                            d.elements.append(t)
                            c.elements.remove(t)
                            d.calculateCentroid()

alg=kmeansClusterer()
alg.initializeCluster()
#for i in range(k):
#    print(alg.clusters[i].centroid, " ",alg.clusters[i].elements)

alg.calculateCluster()
for i in range(k):
    print(alg.clusters[i].centroid, " ",alg.clusters[i].elements)
#print(alg.clusters[0].elements)
#print(alg.clusters[1].elements)
#print(alg.clusters[2].elements)

    