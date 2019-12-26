# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:40:37 2019

@author: Daniel
"""

def findMaxPalindrome(currValue, maxRange, minRange):
    for countA in range(maxRange, minRange, -1):
        maxValue = countA * maxRange
        if(maxValue < currValue):
            return(currValue)
        for countB in range(maxRange, minRange, -1):
            result = countA * countB
            if(result > currValue):
                strResult = str(result)
                if(strResult == strResult[::-1]):
                    currValue = result

def test_findMaxPalindrome():
    assert findMaxPalindrome(currValue = 0, maxRange = 100,minRange = 1) == 9009, "Max two digit palindrome should be 9009"

test_findMaxPalindrome()
print(findMaxPalindrome(currValue = 0, maxRange = 999, minRange = 0))