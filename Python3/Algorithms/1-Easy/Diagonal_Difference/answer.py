#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    size = len(arr)
    left_diag = 0
    right_diag = 0

    for i in range(0,size):
        left_diag += arr[i][i]
    for i in range(0,size):
        right_diag += arr[size-1-i][i]

    return abs(left_diag - right_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
