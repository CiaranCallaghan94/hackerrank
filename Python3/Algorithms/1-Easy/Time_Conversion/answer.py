import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_list = s.split(':')
    # For PM
    if time_list[2][-2]=='P':
        # Check for 12 PM
        if time_list[0]=='12':
            time_list[0]='00'
        time_list[0] = int(time_list[0]) + 12
        time_list[2] = time_list[2][0:2]
        return str(time_list[0]) + ':' + str(time_list[1]) + ':' + str(time_list[2])
    # Check for 12 AM
    elif time_list[0] == '12':
        time_list[0] = '00'
        time_list[2] = time_list[2][0:2]
        return str(time_list[0]) + ':' + str(time_list[1]) + ':' + str(time_list[2])
    else:
        return s[0:-2]

print(timeConversion('12:00:00AM'))
