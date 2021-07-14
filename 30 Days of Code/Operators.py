# Link: https://www.hackerrank.com/challenges/30-operators/problem
# This is Day 2 of 30 Days of Code
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = tip_percent/100*meal_cost
    tax_cost = tax_percent/100*meal_cost
    total_cost = meal_cost+tip_cost+tax_cost
    print(int(round(total_cost,0)))
    return round(total_cost,0)
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
