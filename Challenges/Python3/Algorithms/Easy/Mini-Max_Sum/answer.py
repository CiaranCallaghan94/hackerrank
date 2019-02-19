#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    size = len(arr)
    arr.sort()
    min = sum(arr[0:size-1])
    max = sum(arr[1:size])

    print(f"{min} {max}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
