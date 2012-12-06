'''
2050 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder

What is the smallest number divisible by each of the numbers from 1-20
'''

'''##Slow
Calculate the smallest number evenly divisible by all numbers from
1-ceiling

ceiling - Int - Upper bound for the range of numbers to be used
'''
def evenlyDivisible(ceiling):
    smallestNum = 0
    numList = range(1,ceiling + 1)
    current = 1
    factor = False

    while not factor:
        factor = True
        for num in numList:
            if ceiling * current % num != 0:
                factor = False
                break
        smallestNum = ceiling * current
        current += 1
        
    return smallestNum

print evenlyDivisible(20)
