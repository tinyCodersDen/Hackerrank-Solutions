# Link: https://www.hackerrank.com/challenges/python-tuples/problem

n = input('')
i = input('').split(' ')
i = [int(y) for y in i]
t = tuple(i)
print(hash(t))
