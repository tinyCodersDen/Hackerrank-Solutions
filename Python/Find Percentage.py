# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    var1 = round(sum(student_marks[query_name])/len(student_marks[query_name]),2)
    if len(str(var1).split('.')[1])==1:
        print(str(var1)+'0')
    else:
        print(var1)
