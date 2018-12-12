#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:38:44 2018

@author: vakanto
"""

import math as m
def euclideanDist(a,b):
    result=m.sqrt(sum([m.pow((x-y),2) for x,y in zip(a,b)]))
    return result
