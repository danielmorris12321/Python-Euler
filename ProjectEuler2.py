# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:01:07 2019

@author: demor
"""

limit = 4000000
mod = 2

def fibonacci(limit):
    if(limit < 1):
        fib =  []
    elif(limit < 2):
        fib =  [1]
    elif(limit < 3):
        fib = [1,2]
    else:
        fib = [1,2]
        currValue = 3
        while currValue < limit:
            fib.append(currValue)
            # negative index counts from the end of the list
            currValue = fib[-2] + fib[-1]
        
    return(fib)
   
def subsetList(listInput, mod):
    return[x for x in listInput if x % 2 == 0]

sequence = fibonacci(limit)
sequence = subsetList(sequence, mod)
print(sum(sequence))