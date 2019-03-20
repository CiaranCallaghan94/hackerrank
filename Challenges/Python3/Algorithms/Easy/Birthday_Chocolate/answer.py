#!/bin/python3

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Inputs:
# 5
# 1 2 1 3 2
# 3 2

import math
import os
import random
import re
import sys

# Complete the birthday function below.
# Time complexity =
# Space complexity =
def birthday(s, d, m):
    total_matches = 0
    count = 0
    start_pointer = 0
    end_pointer = m
    while end_pointer <= len(s):
        if sum(s[start_pointer:end_pointer]) == d:
            count += 1
        start_pointer += 1
        end_pointer +=1
    return count

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
