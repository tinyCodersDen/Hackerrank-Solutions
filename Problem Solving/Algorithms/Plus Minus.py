# Link: https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l = [0,0,0]
    for y in arr:
        if y>0:
            l[0]+=1
        elif y<0:
            l[1]+=1
        elif y==0:
            l[2]+=1
    for t in l:
        print(t/len(arr))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
