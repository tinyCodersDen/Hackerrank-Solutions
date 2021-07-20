# Link: https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    s = input()
    l = [False]*5
    for t in s:
        if t.isalnum():l[0]=True
        if t.isalpha():l[1]=True
        if t.isdigit():l[2]=True
        if t.islower():l[3]=True
        if t.isupper():l[4]=True
for y in l: print(y)
