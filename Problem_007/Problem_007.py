'''
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
'''

def getPrime(index):
    primes = [2,3]
    num = 1
    
    while len(primes) < index:
        if isPrime(6 * num - 1):
            primes.append(6 * num - 1)
        if isPrime(6 * num + 1):
            primes.append(6 * num + 1)
        num += 1
        
    return primes[-1]
        
def isPrime(number):
    factors = getFactors(number)
    return len(factors) == 1
    
def getFactors(number):
    factor = 2
    factors = []
    
    while factor <= number:
        if(number % factor == 0):
            number = number / factor
            factors.append(factor)
            factor -= 1     
        factor += 1
    
    return factors

print getPrime(10001)