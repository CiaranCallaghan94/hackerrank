#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_list = s.split(':')
    if time_list[2][-2]=='P':
        if time_list[0]=='12':
            time_list[0]='00'
        time_list[0] = int(time_list[0]) + 12
        time_list[2] = time_list[2][0:2]
        return str(time_list[0]) + ':' + str(time_list[1]) + ':' + str(time_list[2])
    elif time_list[0] == '12':
        time_list[0] = '00'
        time_list[2] = time_list[2][0:2]
        return str(time_list[0]) + ':' + str(time_list[1]) + ':' + str(time_list[2])
    else:
        return s[0:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
