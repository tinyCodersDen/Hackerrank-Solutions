# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    print(str(arr[0]+arr[1]+arr[2]+arr[3])+' '+str(arr[-1]+arr[-2]+arr[-3]+arr[-4]))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
