# Link: https://www.hackerrank.com/challenges/swap-case/problem
import string
def swap_case(i):
    upper_letters = list(string.ascii_uppercase)
    lower_letters = list(string.ascii_lowercase)
    string1 = ''
    for y in i:
        if y in upper_letters:
            index = upper_letters.index(y)
            string1+=lower_letters[index]
        elif y in lower_letters:
            index = lower_letters.index(y)
            string1+=upper_letters[index]
        else:
            string1+=y
    return string1
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
