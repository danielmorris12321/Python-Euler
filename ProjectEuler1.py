# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:52:25 2019

@author: Daniel
"""

def test_sumCounter():
    assert sumCounter(10) == 23, "Sum of natural numbers below 10 multiples of 3 and 5 should be 23"

def sumCounter(limit):
    sum = 0
    for i in range(1,limit):
        if(i % 3  == 0) or (i % 5 == 0):
            sum = sum + i    
    return(sum)

test_sumCounter()
print(sumCounter(1000))    