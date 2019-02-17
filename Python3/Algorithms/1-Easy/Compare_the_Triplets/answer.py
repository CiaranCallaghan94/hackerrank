#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_p = 0
    bob_p = 0
    for i in range(0,3):
        if a[i]>b[i]:
            alice_p += 1
        elif b[i]>a[i]:
            bob_p += 1

    return [alice_p,bob_p]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
