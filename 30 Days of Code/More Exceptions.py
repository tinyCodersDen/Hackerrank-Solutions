# Link: https://www.hackerrank.com/challenges/30-more-exceptions/problem
# This is Day 17 of 30 Days of Code
class Calculator():
    def __init__(self):
        pass
    def power(self,n,p):
        if n>=0 and p>=0:
            return n**p
        else:
            return 'n and p should be non-negative'
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)  
