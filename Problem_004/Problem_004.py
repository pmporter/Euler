'''
A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
'''
import math

'''
Finds the largest palindromic number from the product of two n-digit
numbers, where n is digitCount

digitCount - Int - the number of digits
'''
def largestPalindrome(digitCount):
    ceiling = int(math.pow(10, digitCount) - 1)
    operandA = ceiling
    operandB = ceiling
    product = 0
    palindrome = 0
    
    while operandA > 0:
        
        while operandB > ceiling / 2:
            product = operandA * operandB
            
            if isPalindrome(product) == 1:
                palindrome = product if product > palindrome else palindrome
                
            operandB -= 1
        #end while        
        operandA -= 1
        operandB = ceiling
        
    #end while
    return palindrome

'''
Checks a number for palindromicity (is that a word?)

num - Int - the number to check
'''
def isPalindrome(num):
    return 1 if str(num)[::-1] == str(num) else 0
    
#
print largestPalindrome(3)
