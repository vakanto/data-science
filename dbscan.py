input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]


def euclideanDist(a,b):
    p1=[a.xValue, a.yValue]
    p2=[b.xValue, b.yValue]
    
    result=m.sqrt(sum([m.pow((x-y),2) for x,y in zip(p1,p2)]))
    return result

class Point():
    def __init__(self,x,y):
        self.xValue=x
        self.yValue=y
        self.clusterID=none

def initializePoints(p):
    point=Point()
    print(p[0])
    point.xValue=p[0]
    point.yValue=p[1]
    return point

class dbScanner:
    def __init__(self, minPoints):
        self.clusters=[]
        self.points=[]
        self.minPoints=minPoints
        for p in input:
            self.points.append(initializePoints(p))
        print(points[0].clusterID)

    def dbScan():
        C=0
        id=0
        for p in self.points:
            if p.clusterID==none:
                if self.expandCluster(self.points, p, id, range, minPoints):
                    id+=1

    def expandCluster(points, startObject, id, range, minPoints):
        seeds=[]
        seeds=self.getNeighbours(startObject, range)

        if len(seeds)<minPoints:
            startObject.clusterID=NOISE
            return false
        #startObject is core-object
        core=startObject
        for seed in seeds:
            seed.clusterID=id
            seeds.remove(core)

            while seeds:
                length=len(seeds)
                counter=0
                object=seeds.get(0)
                neighbours=getNeighbours(object, range)
                if neighbours>=minPoints:
                    for neighbour in neighbours:
                        if neighbour.clusterID==NOISE or neighbour.clusterID==none:
                            if neighbour.clusterID==none:
                                seeds.append(neighbour)
                            neighbour.clusterID=id
                counter+=1
                counter=counter%length
            seeds.remove(seed)
        return true

    def getNeighbours(point, range):
        #naiv
        neighbours=[]
        for p in self.points:
            distance=euclideanDist(point, p)
            if distance <= range:  
                neighbours.append(p)
        return neighbours

def clusterPlot(clusters):
    import matplotlib.pyplot as plot
    import numpy as np

    #fig = plot.figure()
    plot.figure()
    for c in clusters:
        elements=[]
        for p in c.points:
            point=[p.xValue, p.yValue]
            elements.append(point)

        elems = np.array(elements)
        plt.scatter(elems[:,0], elems[:,1])
        #centroid = c.centroid
        #plt.plot(centroid[0], centroid[1], 'X', c='black')
    plt.show()

dbScanner=dbScanner(3)
dbScanner.dbScan()
clusterPlot(dbScanner.clusters)