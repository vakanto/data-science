#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:06:44 2018

@author: tobias
"""
import createInput
import distFunctions as dist
#input=[[1,5],[6,2],[8,1],[3,5],[2,4],[2,6],[6,1],[6,8],[7,3],[7,6],[8,3],[8,7],[3,4],[2,9],[6,7],[2,1]]
input=createInput.create2dimensionalList(100)
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
                p.used=True
                output.append(p)
                self.expandClusterOrder(p)
                
    def neighbours(self, point):
        neighbours=[]
        for p in self.points:
            distance=euclideanDist(point, p)
            if  distance<self.width:
                neighbours.append(p)
        return neighbours
    
    def coreDistance(self,neighbours):
        corePoints=[]
        neighbours=sorted(neighbours, key=lambda Point: Point.reachableDistance)
        for i in range(self.minPoints):
            corePoints.append(neighbours[i])
            #print max([x.reachableDistance for x in corePoints])
        return max([x.reachableDistance for x in corePoints])
    
    
    
    def expandClusterOrder(self, point):
        neighbours=self.neighbours(point)
        point.used=True
        output.append(point)
        if len(neighbours)>=self.minPoints:
            for p in neighbours:
                p.reachableDistance=euclideanDist(p, point)
            point.coreDistance=self.coreDistance(neighbours)
            self.orderSeeds(point, neighbours)
            
            for p in point.seeds:
                point = p
                neighbours=self.neighbours(point)
                if neighbours >= self.minPoints:
                    point.coreDistance=self.coreDistance(neighbours)
                    point.used=True
                    output.append(point)
                    self.orderSeeds(point, neighbours)
            
        self.points.remove(point)
            
            
    def orderSeeds(self, core, neighbours):   
        neighbours.remove(core)
        coreDist=core.coreDistance  
        if core.seeds==[]:
            for p in neighbours:
                core.seeds.append(p)
        for p in neighbours:
            if p.used==False:
                new_r_dist=min(coreDist, euclideanDist(core, p))
     
                if new_r_dist < p.reachableDistance:
                    p.reachableDistance=new_r_dist
        sorted(core.seeds)
        #äprint core.seeds
        
optics=opticsScanner(2, 400)
optics.generateDiagram(optics.points)
for p in output:
    print p
    print p.reachableDistance
    
import plotFunctions as plot

plot.pointPlot(output)

        
        
        
        
        
        
        
        