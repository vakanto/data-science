#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:57:54 2018

@author: tobias
"""

def create2dimensionalList(size):
    import random
    input=[]
    for i in range(size):
        a=random.randint(0, 1000)
        b=random.randint(0, 1000)
        l=[a,b]
        input.append(l)
    return input