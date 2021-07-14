# Link: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    
    num1,num2,num3 = year/4,year/100,year/400
    if num1 == int(num1) and num2!=int(num2):
        leap = True
    if num3 == int(num3):
        leap = True
    return leap

year = int(input())
print(is_leap(year))
