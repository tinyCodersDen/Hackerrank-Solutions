# Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# This is Day 25 of 30 Days of Code
import math
r = int(input(''))
def Prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i is 0:
            return False
    return True
for t in range(r):
    ask = int(input(''))
    if ask>=2 and Prime(ask):
        print('Prime')
    else:
        print('Not prime')
