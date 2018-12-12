#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:48:40 2018

@author: tobias
"""

def pointClusterPlot(clusters):
    import matplotlib.pyplot as plt
    import numpy as np

    #fig = plot.figure()
    plt.figure()
    for c in clusters:
        elements=[]
        for p in c.elements:
            point=[p.xValue, p.yValue]
            elements.append(point)

        elems = np.array(elements)
        plt.scatter(elems[:,0], elems[:,1])
        #centroid = c.centroid
        #plt.plot(centroid[0], centroid[1], 'X', c='black')
    
    plt.show()
    
def interactiveClusterPlot(clusters):
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
        
def listClusterPlot(clusterList):
    import matplotlib.pyplot as plt
    import numpy as np

    #fig = plot.figure()
    plt.figure()
    for c in clusterList:
        elems = np.array(c.elements)
        plt.scatter(elems[:,0], elems[:,1])
        plt.plot(c.centroid[0], c.centroid[1], 'X', c='black')
        #centroid = c.centroid
        #plt.plot(centroid[0], centroid[1], 'X', c='black')
    
    plt.show()