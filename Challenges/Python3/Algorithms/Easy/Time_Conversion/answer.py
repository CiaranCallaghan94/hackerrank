#!/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem
import os
import sys

def timeConversion(s):
    # PM
    if s[-2:-1]=='P':
        if s[:2]=='12':
            return '12' + s[2:-2]
        return str(int(s[:2])+12) + s[2:-2]
    # AM
    if  s[:2] == '12':
        return '00' + s[2:-2]
    return s[0:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
