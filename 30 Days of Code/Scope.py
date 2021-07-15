# Link: https://www.hackerrank.com/challenges/30-scope/problem
# This is Day 14 of 30 Days of Code
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for t,e in enumerate(self.__elements):
            if self.__elements[-1]!=e:
                self.r = abs(e-self.__elements[t+1])
                if self.r>self.maximumDifference:
                    self.maximumDifference=self.r
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
