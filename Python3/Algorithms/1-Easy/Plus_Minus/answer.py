#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #  positive, negative and 0 values all divided by size of array
    size = len(arr)
    pos=0
    neg=0
    zero=0
    for i in range (0,size):
        val = arr[i]
        if val>0:
            pos += 1
        elif val<0:
            neg += 1
        else:
            zero += 1

    print(pos/size)
    print(neg/size)
    print(zero/size)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
