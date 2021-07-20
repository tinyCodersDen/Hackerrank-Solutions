# Link: https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    for x in range(0,len(string),max_width):
        if x+max_width>len(string):
            break
        else:
            print(string[x:x+max_width])
    return string[x:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
