# Link: https://www.hackerrank.com/challenges/30-bitwise-and/problem
# This is Day 29 of 30 Days of Code
# This is also the final Day
T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)
