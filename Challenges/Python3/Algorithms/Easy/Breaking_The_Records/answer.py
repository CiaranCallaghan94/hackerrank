#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
