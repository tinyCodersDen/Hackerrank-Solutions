# Link: https://www.hackerrank.com/challenges/30-recursion/problem
# This is Day 9 of 30 Days of Code
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==1:
        return 1
    else:
        n = n*factorial(n-1)
    return n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
