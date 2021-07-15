# Link: https://www.hackerrank.com/challenges/30-arrays/problem
# This is Day 7 of 30 Days of Code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = arr[::-1]
    print(' '.join(list(map(str,arr))))
