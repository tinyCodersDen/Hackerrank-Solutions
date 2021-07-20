# Link: https://www.hackerrank.com/challenges/matrix-script/problem
import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string = ''
for x in range(m):
    for t in matrix:
        string+=t[x]
print(string)
