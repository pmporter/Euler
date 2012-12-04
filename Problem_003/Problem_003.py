'''
Find the largest prime factor of a composite number
'''
number = 600851475143
primeFactors = []

'''
'''
def getPrimeFactors(num):
    currentPrime = 2
    
    while currentPrime < (num / 2):    
        if(num % currentPrime == 0):
            primeFactors.append(currentPrime)
            currentPrime = getNextPrime(currentPrime)
        else:
            currentPrime = getNextPrime(currentPrime)
        
    return primeFactors

'''
'''
def getNextPrime(num):
    if checkPrimality(num+1) == 1:
        return num + 1
    else:
        return getNextPrime(num+1)

'''
'''
def checkPrimality(num):
    isPrime = 1
    i = 3
    
    while i < num and isPrime:
        if(num % i == 0):
            isPrime = 0
        i += 2
    
    return isPrime

print getPrimeFactors(number)            
    
                
            
        
        