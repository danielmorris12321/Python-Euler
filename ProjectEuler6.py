# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:50:15 2020

@author: Daniel
"""

def sumOfSquares(maxCount):
    totalSum = 0
    for i in range(1, maxCount + 1):
        totalSum += i **2
    return(totalSum)
    
def squareOfSum(maxCount):
    totalSum = 0
    for i in range(1, maxCount + 1):
        totalSum += i
    totalSum = totalSum**2
    return(totalSum)
    
def calculateDifference(maxCount):
    sumSquares = sumOfSquares(maxCount)
    squareSums = squareOfSum(maxCount)
    print("Sum of squares equals " + str(sumSquares))
    print("Square of sums equals " + str(squareSums))
    diff = squareSums - sumSquares
    print("Difference equals " + str(diff))
    return(diff)
    
def testFunction():
    assert calculateDifference(10) == 2640, "Difference for 10 should be 2640"
    
testFunction()
calculateDifference(100)