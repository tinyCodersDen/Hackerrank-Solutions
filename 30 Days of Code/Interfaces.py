# Link: https://www.hackerrank.com/challenges/30-interfaces/problem
# This is Day 19 of 30 Days of Code
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        calc = []
        for i in range(1, n+1):
            if n%i == 0:
                calc.append(i)
        return sum(calc)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
