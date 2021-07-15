# Link: https://www.hackerrank.com/challenges/30-review-loop/problem
# This is Day 6 of 30 Days of Code
n = int(input(''))
for r in range(n):
    a = input('')
    odd = ''
    even = ''
    bool=True
    for t in a:
        if bool==True:
            even+=t
            bool=False
        elif bool!=True:
            odd+=t
            bool=True
    print(even,odd)
