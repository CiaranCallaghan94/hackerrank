#!/bin/python3
# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    # OPTION 1: Brute force
    # if v1 <= v2:
    #     return 'NO'
    # while True:
    #     if x1 == x2:
    #         return 'YES'
    #     elif x1 > x2:
    #         return 'NO'
    #     x1 += v1
    #     x2 += v2

    # OPTION 2: Math
    if v1 <= v2:
        return 'NO'
    if not (x1 - x2) % (v2 - v1) == 0:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
