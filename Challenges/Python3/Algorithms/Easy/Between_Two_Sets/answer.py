#!/bin/python3
# https://www.hackerrank.com/challenges/between-two-sets/problem
import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    add = True
    nums = []
    amax = max(a)
    bmin = min(b)
    currentVal = amax
    while currentVal <= bmin:
        for num in a:
            if not currentVal % num == 0:
                add = False
        if add:
            nums.append(currentVal)
        add = True
        currentVal += amax

    newnums = nums.copy()
    for n in nums:
        print(n)
        for num in b:
            if not num % n == 0:
                if n in newnums:
                    newnums.remove(n)
                    pass

    return len(newnums)




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
