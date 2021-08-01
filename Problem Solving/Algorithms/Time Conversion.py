# Link: https://www.hackerrank.com/challenges/time-conversion/problem
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    zone = s[-2]+s[-1]
    s=s[:-2]
    s2 = s.split(':')
    if zone=='AM':
        if s2[0]=='12':
            s2[0]='00'
            string1=''
            for t in s2:
                string1+=t
                string1+=':'
            string1=string1[:-1]
            return string1
        else:
            return s
    else:
        if s2[0]=='12':
            return s
        else:
            s2[0]=str(int(s2[0])+12)
            string1=''
            for t in s2:
                string1+=t
                string1+=':'
            string1=string1[:-1]
            return string1

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
