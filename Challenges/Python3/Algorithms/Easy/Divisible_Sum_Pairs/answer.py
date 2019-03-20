#!/bin/python3

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Input:
# 6 3
# 1 3 2 6 1 2

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ar.sort()
    print(ar)
    number_pairs = 0
    for i in range(n-1):
        for j in range (n-i-1):
            print(f"{ar[i]} + {ar[i+j+1]} % {k} == 0" )
            if ar[i] <= ar[i+j+1] and (((ar[i] + ar[i+j+1]) % k) == 0):
                print('True')
                number_pairs += 1
    return number_pairs

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
