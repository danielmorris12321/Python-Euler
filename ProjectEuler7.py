# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:07:38 2020

@author: Daniel
"""

def checkPrime(n):
    if n < 2: return "Not prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculatePrime(n):
    numPrimes = 0
    currPrime = 1
    while numPrimes < n:
        currPrime += 1
        if checkPrime(currPrime):
            numPrimes += 1
    return currPrime

print(calculatePrime(1001))