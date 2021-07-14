# Link: https://www.hackerrank.com/challenges/s10-standard-deviation/problem
# This is Day 1 of 10 Days of Statistics

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)
    s = 0
    for t in arr:
        r=t-mean
        r=r*r
        s+=r
    s=s/len(arr)
    s=math.sqrt(s)
    print(round(s,1))
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
