# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
def top_area(x,y):
    times = (x-1)//2
    l = []
    string1 = '.|.'
    count=3
    c = (y-len(string1))//2
    string2 = '-'*c
    string2+=string1
    string2 +='-'*c
    l.append(string2)
    print(string2)
    for t in range(times-1):
        string1 = '.'
        for n in range(count-1):
            string1+='|..'
        string1+='|.'
        c = (y-len(string1))//2
        string2 = '-'*c
        string2+=string1
        string2 +='-'*c
        print(string2)
        l.append(string2)
        count+=2
    return l
        
ask = input('').split(' ')
ask = [int(s) for s in ask]
key = top_area(ask[0],ask[1])
c = (ask[1]-len('WElCOME'))//2
string='-'*c
string+='WELCOME'
string+='-'*c
print(string)
for t in key[::-1]:
    print(t)
