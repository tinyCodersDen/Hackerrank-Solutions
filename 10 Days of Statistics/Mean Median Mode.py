# Link: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# This is Day 0 of 10 Days of Statistics
n = int(input(''))
t = list(map(int,input('').split(' ')))
mean = sum(t)
mean = mean/len(t)
print(mean)
median = len(t)
if median%2==0:
    u = t.copy()
    u.sort()
    median=int(median/2)
    median = u[median-1]+u[median]
    median=median/2
    print(median)
else:
    u = t.copy()
    u.sort()
    median-=1
    median=median/2
    median=u[median]
    print(median)
mode = max(sorted(t), key=t.count)
print(mode)
