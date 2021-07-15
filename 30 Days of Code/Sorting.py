# Link: https://www.hackerrank.com/challenges/30-sorting/problem
# This is Day 20 of 30 Days of Code
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    ba = 0
    list1 = a
    list2 =list1.copy()
    list2.sort()
    if list1!=list2:
        for x in range(len(list1)):
            for j in range(0,len(list1)-x-1):
                if list1[j]>list1[j+1]:
                    list1[j],list1[j+1]=list1[j+1],list1[j]
                    ba+=1
    print('Array is sorted in '+str(ba)+" swaps.")    
    print('First Element: '+str(list1[0]))
    print('Last Element: '+str(list1[-1]))
