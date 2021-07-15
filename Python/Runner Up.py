# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = input('').split(' ')
    arr = [int(o) for o in arr]
    arr = set(arr)
    arr = list(arr)
    arr.remove(max(arr))
    print(max(arr))
