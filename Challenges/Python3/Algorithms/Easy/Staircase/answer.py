#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces = n-1
    hashes = 1
    while spaces >= 0:
        print((' ' * spaces) + ('#' * hashes))
        hashes += 1
        spaces -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
