'''
By considering the terms in the Fibonacci sequence whose values 
do not exceed four million (4,000,000), find the sum of the 
even valued terms
'''
import math

'''
Inverse Sqrt
    f(n) = Floor(phi^n / sqrt(5) + .5)
    where phi = (1 + sqrt(5)) / 2
'''
def inverseFib(n):
    inverseSqrt5 = 1 / math.sqrt(5)
    phi = (1 + math.sqrt(5)) / 2
    
    return int(math.floor(math.pow(phi, n) * inverseSqrt5 + .5))

'''
Recursive - Slow
    f(n) = f(n-1) + f(n-2)
'''
def fib(n):
    return n if n < 2 else (fib(n-1) + fib(n-2))

## Solution Calculation
sumOfEvens = 0
upperBound = 4000000
current = 0
index = 0

while current < upperBound:
    current = inverseFib(index)
    if current % 2 == 0:
        sumOfEvens += current
    index += 1

print sumOfEvens