#!/bin/python3
# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# 7 11 -> start 7 end 11
# 5 15 -> apple tree 5 orange tree 15
# 3 2 -> null null
# -2 2 1 -> apples
# 5 -6 -> oranges

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0

    for app in apples:
        x = a + app
        if x >= s and x <= t:
            apples_on_house += 1

    for oran in oranges:
        x = b + oran
        if x >= s and x <= t:
            oranges_on_house += 1

    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
