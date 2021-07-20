# Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
x = input('').split(' ')
x[1] = int(x[1])
list1 = list(permutations(x[0],x[1]))
list1 = sorted(list1)
for t in list1:
    string1 = ''
    for s in t:
        string1+=s
    print(string1)
