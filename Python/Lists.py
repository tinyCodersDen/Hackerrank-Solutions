# Link: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for t in range(N):
        ask = input('').split(' ')
        if ask[0]=='print':print(l)
        elif ask[0]=='insert':l.insert(int(ask[1]),int(ask[2]))
        elif ask[0]=='reverse': l = l[::-1]
        elif ask[0]=='append': l.append(int(ask[1]))
        elif ask[0]=='sort': l.sort()
        elif ask[0]=='pop': l.pop()
        elif ask[0]=='remove': l.remove(int(ask[1]))
