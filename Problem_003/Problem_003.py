'''
Find the largest prime factor of a composite number
'''
import time

def largestPrimeFactor(num):
    factor = 2
    
    start = time.time() 
    while factor <= num:
        if(num % factor == 0):
            num = num / factor
            factor -= 1     
        factor += 1
    end = time.time()
    
    print end-start
    return factor

number = 600851475143
print largestPrimeFactor(number)

                
            
        
        