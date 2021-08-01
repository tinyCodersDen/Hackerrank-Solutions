# Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    counts = [0,0]
    for t,j in enumerate(a):
        if j>b[t]:
            counts[0]+=1
        elif j<b[t]:
            counts[1]+=1
    return counts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
