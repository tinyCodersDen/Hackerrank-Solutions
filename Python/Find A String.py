# Link: https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count=0
    for t in range(0,len(string)-len(sub_string)+1):
        sub = string[t:t+len(sub_string)]
        if sub==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
