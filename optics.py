#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:06:44 2018

@author: tobias
"""
import createInput
import distFunctions as dist
#input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]
pointCount=80
input=createInput.create2dimensionalList(pointCount)
output=[]

def initializePoints(p):
    point=Point(p[0], p[1])
    return point

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
        self.core=False
        self.reachableDistance=None
        self.used=False
        self.coreDistance=None
        self.seeds=[]
    def __str__(self):
        return "(" + str(self.xValue) + " , " + str(self.yValue) +")"

class opticsScanner():
    
    def __init__(self, minPoints, width):
        self.points=[]
        self.minPoints=minPoints
        self.width=width
        
        for p in input:
            self.points.append(initializePoints(p))
            
    def generateDiagram(self, points):
        for p in self.points:
            if p.used==False:
                self.expandClusterOrder(p)
                
    def neighbours(self, point):
        neighbours=[]
        for p in self.points:
            distance=euclideanDist(point, p)
            #if distance == 0:
            if distance<self.width:
                neighbours.append(p)
                if p.core==False and p!=point:
                    p.reachableDistance=distance
        return neighbours
    
    def coreDistance(self,neighbours):
        corePoints=[]
        #Entnimm die ersten minPoint Elemente
        corePoints=neighbours[:self.minPoints]
        #Gib die Kern-Distanz zurück
        if len(corePoints)>1:
            return max([x.reachableDistance for x in corePoints if x.reachableDistance!=None])
        else:
            return -1
    
    
    def expandClusterOrder(self, point):
        neighbours=[]
        neighbours.append(point)
        temp=self.neighbours(point)
        temp.remove(point)
        #Sortiere die Nachbarn nach Erreichbarkeitsdistanz
        temp=sorted(temp, key=lambda Point: Point.reachableDistance)
        neighbours=neighbours+temp
        point.used=True
        point.reachableDistance=None
        
        if len(neighbours)>=self.minPoints:
            #point ist Kern Objekt
            neighbours.remove(point)           
            point.coreDistance=self.coreDistance(neighbours)
            point.core=True
            output.append(point)
            orderSeeds=neighbours
            orderSeeds=self.updateSeeds(point, neighbours, orderSeeds)
            point.reachableDistance=None
            
            i=0
            while i==0:
                if orderSeeds == []:
                    i=1
                else:    
                    new_point=orderSeeds[0]
                    new_point.used=True
                    new_point_neighbours=self.neighbours(new_point)
                    
                    if len(new_point_neighbours)>=self.minPoints:
                        new_point.core==True
                        new_point_neighbours.remove(new_point)
                        new_point.coreDistance=self.coreDistance(new_point_neighbours)
                        orderSeeds=self.updateSeeds(new_point, new_point_neighbours, orderSeeds)
                    orderSeeds.remove(new_point)
                    output.append(new_point)
                    print(new_point.reachableDistance)
        else:
            output.append(point)
        #self.points.remove(point)
            
            
    def updateSeeds(self, core, neighbours, orderSeeds):   
        for p in neighbours:
            if p.used==False:
                new_r_dist=max(core.coreDistance, p.reachableDistance)
                if new_r_dist < p.reachableDistance or p.reachableDistance==0:
                    p.reachableDistance = new_r_dist
            if p not in orderSeeds and p.used==False:
               orderSeeds.append(p)
               
        orderSeeds=sorted(orderSeeds, key=lambda Point: Point.reachableDistance)
        
        return orderSeeds
        
optics=opticsScanner(3, 100)
optics.generateDiagram(optics.points)
#for p in output:
#    print p.reachableDistance
    
#import plotFunctions as plot

class Cluster():
    def __init__(self, elements, id):
        self.elements=elements
        self.id=id

counter=0
clusters=[]

counter=0
noise=Cluster([], 999)
clusters.append(noise)
cluster=Cluster([],0)
for p in output:
    print(p.reachableDistance)
    if p.core==True and p.reachableDistance==None:
        cluster=Cluster([],counter)
        counter+=1
        cluster.elements.append(p)
        clusters.append(cluster)
        #print("Core")
        #print(p)
    else:
        if p.reachableDistance==None:
            #print("Noise")
            noise.elements.append(p)
            #print "noise"
            #print(p)
        else:
            cluster.elements.append(p)
            #print("Element")
            #print(p)


import plotFunctions as plot
plot.pointClusterPlot(clusters)
maxHeight=max([x.reachableDistance for x in output if x.reachableDistance!=None])+50
for x in output:
    #print x.reachableDistance
    if x.reachableDistance==None:
        #print(x)
        x.reachableDistance=maxHeight
from matplotlib import pyplot as plt
xValues=range(pointCount)
yValues=[y.reachableDistance for y in output]
plt.bar(xValues, yValues, width=1)
plt.show()      

for c in clusters:
    print(c.id)
    for p in c.elements:
        print(p)
    print("==========================")        
        
        
        
        
        