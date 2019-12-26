# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:52:25 2019

@author: Daniel
"""
sum = 0

for i in range(1,1000):
    if(i % 3  == 0) or (i % 5 == 0):
        sum = sum + i    
print(sum)