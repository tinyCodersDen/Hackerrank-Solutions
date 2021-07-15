# Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# This is Day 16 of 30 Days of Code
import sys

S = input().strip()
try:
    S = int(S)
    print(S)
except ValueError:
    print('Bad String')
