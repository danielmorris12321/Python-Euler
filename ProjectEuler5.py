# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:05:46 2020

@author: Daniel
"""
        
def checkDivs(num, maxRange):
    for i in range(1,maxRange):
        if num % i != 0:
            return False
    return True
    
def generateResult(num,maxRange):
    while True:
      if checkDivs(num, maxRange):
        print(num)
        break
      else:
        num = num + 20
   
generateResult(2520,20)     
