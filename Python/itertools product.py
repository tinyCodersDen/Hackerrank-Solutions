# Link: https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product
y = input('').split(' ')
z = input('').split(' ')
y = [int(t) for t in y]
z = [int(d) for d in z]
l = list(product(y,z))
l = sorted(l)
string1 = ''
for t in l:
    w = str(t)
    string1+=w
    string1+=' '
print(string1)
