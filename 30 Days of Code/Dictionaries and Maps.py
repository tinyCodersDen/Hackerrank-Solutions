# Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# This is Day 8 of 30 Days of Code
t = int(input(''))
dict1 = {}
for q in range(t):
    a = list(input('').split(' '))
    dict1[a[0]]=int(a[1])
for y in range(t):
    try:
        j = input('')
        if j in dict1:
            h = dict1[j]
            print(j+'='+str(h))
        else:
            print('Not found')
    except EOFError:
        break
