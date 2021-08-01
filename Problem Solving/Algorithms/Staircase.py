# Link: https://www.hackerrank.com/challenges/staircase/problem
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for x in range(1,n+1):
        string1=' '*(n-x)
        string1+=('#'*x)
        print(string1)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
