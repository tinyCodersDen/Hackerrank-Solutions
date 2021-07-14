# Link: https://www.hackerrank.com/challenges/30-loops/problem
# This is Day 5 of 30 Days of Code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for t in range(1,11):
        print(str(n)+' '+'x'+' '+str(t)+' '+'='+' '+str(t*n))
