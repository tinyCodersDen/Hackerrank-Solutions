# Link: https://www.hackerrank.com/challenges/grading/problem
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    l = []
    for t in grades:
        if t<38:
            l.append(t)
            continue
        if int(str(t)[-1])>5:
            t1 = str(t)
            t1 = t1[:-1]
            t1 = int(t1)
            t1+=1
            t1=str(t1)
            t1+='0'
            print(t1)
        else:
            t1 = str(t)
            t1 = t1[:-1]
            t1+='5'
        num1 = int(t1)-t
        if num1<3:
            l.append(t1)
        else:
            l.append(t)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
