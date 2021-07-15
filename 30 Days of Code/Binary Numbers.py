# Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# This is Day 10 of 30 Days of Code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = bin(n)
    b = str(b)
    b = b[2:]
    r = b.split('0')
    max_len = 0
    for t in r:
        if max_len<len(t):
            max_len=len(t)
    print(max_len)
