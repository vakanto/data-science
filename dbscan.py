#input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]

import random
input=[]
for i in range(100):
    a=random.randint(0, 10000000)
    b=random.randint(0, 10000000)
    l=[a,b]
    print(l)
    input.append(l)

def euclideanDist(a,b):
    import math as m
    p1=[a.xValue, a.yValue]
    p2=[b.xValue, b.yValue]
    
    result=m.sqrt(sum([m.pow((x-y),2) for x,y in zip(p1,p2)]))
    return result

class Point():
    def __init__(self,x,y):
        self.xValue=x
        self.yValue=y
        self.clusterID=None

class Cluster():
    def __init__(self, elements, id):
        self.elements=elements
        self.id=id



def initializePoints(p):
    point=Point(p[0], p[1])
    #print(p[0])
    return point

class dbScanner:
    def __init__(self, minPoints, width):
        self.clusters=[]
        self.points=[]
        self.minPoints=minPoints
        self.width=width
        for p in input:
            self.points.append(initializePoints(p))
        #print(points[0].clusterID)

    def dbScan(self):
        C=0
        id=0
        for p in self.points:
            #print(p)
            if p.clusterID==None:
                neighbours=self.expandCluster(self.points, p, id, self.width, self.minPoints)
                #print(neighbours)
                if len(neighbours)>0:
                    cluster = Cluster(neighbours, id)
                    id+=1
                    self.clusters.append(cluster)
                    #print(cluster.elements)

    def getNeighbours(self, point, width):
        #naiv
        neighbours=[]
        for p in self.points:
            distance=euclideanDist(point, p)
            if distance <= width:  
                neighbours.append(p)
        return neighbours

    def expandCluster(self, points, startObject, id, width, minPoints):
        seeds=[]
        seeds=self.getNeighbours(startObject, width)
        print(len(seeds))

        if len(seeds)<minPoints:
            startObject.clusterID="NOISE"
            return []
        #startObject is core-object
        core=startObject
        seeds.remove(core)
        for seed in seeds:
            seed.clusterID=id
            for seed in seeds:
                length=len(seeds)
                counter=0
                neighbours=self.getNeighbours(seed, self.width)
                if len(neighbours)>=minPoints:
                    for neighbour in neighbours:
                        if neighbour.clusterID=="NOISE" or neighbour.clusterID==None:
                            if neighbour.clusterID==None:
                                seeds.append(neighbour)
                            neighbour.clusterID=id
                counter+=1
                counter=counter%length
            #seeds.remove(seed)
        return seeds

def clusterPlot(clusters):
    import matplotlib.pyplot as plt
    import numpy as np

    #fig = plot.figure()
    plt.figure()
    for c in clusters:
        elements=[]
        print(c)
        for p in c.elements:
            point=[p.xValue, p.yValue]
            elements.append(point)

        elems = np.array(elements)
        print(elems)
        plt.scatter(elems[:,0], elems[:,1])
        #centroid = c.centroid
        #plt.plot(centroid[0], centroid[1], 'X', c='black')
    
    plt.show()

dbScanner=dbScanner(5, 1000000)
dbScanner.dbScan()
print(dbScanner.clusters)
clusterPlot(dbScanner.clusters)