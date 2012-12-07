'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''
import math

def getSumOfSquares(ceiling):
    return math.pow(ceiling,3)/3 + math.pow(ceiling,2)/2 + ceiling/6

def getSquareOfSum(ceiling):
    return math.pow(((math.pow(ceiling,2) + ceiling) / 2),2)

print int(getSquareOfSum(100) - getSumOfSquares(100))