# Link: https://www.hackerrank.com/challenges/30-regex-patterns/problem
# This is Day 28 of 30 Days of Code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if '@gmail.com' in emailID:
            l.append(firstName)
    for y in sorted(l):
        print(y)
