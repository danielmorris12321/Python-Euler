# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:22:43 2019

@author: Daniel
"""

import math

def test_largestPF():
    assert largestPF(13195) == 29, "Largest prime factor of 13195 should be 29"

def largestPF(n):
    limit = int(math.sqrt(n)) + 1
    for factor in range(2, limit+1):
        while n % factor == 0:
            n /= factor
        if n == 1:
            return factor
    return n

test_largestPF()
print(largestPF(10))