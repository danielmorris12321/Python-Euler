# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:30:05 2020

@author: Daniel
"""

import numpy

def calculateProduct(factors):
    return(numpy.prod(factors))
    
def findTriplet(cap):    
    for a in range(1, cap):
        for b in range(a, cap - a):
            c = cap - a - b
            if a**2 + b**2  == c**2:
                print("Factors: ", a, b, c)
                return([a, b, c])

def main(cap):
    factors = findTriplet(1000)
    print("Sum: ", calculateProduct(factors))
    
main(1000)


