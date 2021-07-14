# Link: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# This is Day 0 of 10 Days of Statistics

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    s = 0
    for t,i in enumerate(X):
        r = i*W[t]
        s+=r
    e = sum(W)
    print(round(s/e,1))
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
