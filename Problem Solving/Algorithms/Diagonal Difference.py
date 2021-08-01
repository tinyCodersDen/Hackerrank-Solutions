# Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    count1 = 0
    sum1 = 0
    for t in arr:
        sum1+=t[count1]
        count1+=1
    count2 = -1
    sum2 = 0
    for t in arr:
        sum2+=t[count2]
        count2-=1
    return abs(sum1-sum2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
