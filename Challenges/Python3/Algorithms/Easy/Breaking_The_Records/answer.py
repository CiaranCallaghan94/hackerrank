#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highscore = None
    lowscore = None
    highbreak = 0
    lowbreak = 0

    for i in scores:
        if highscore is None:
            highscore = i
            lowscore = i
        else:
            if i > highscore:
                highscore = i
                highbreak += 1
            elif i < lowscore:
                lowscore = i
                lowbreak += 1
    return [highbreak,lowbreak]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
