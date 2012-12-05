'''
Find the largest prime factor of a composite number
'''
def largestPrimeFactor(num):
    factor = 2
    
    while factor <= num:
        if(num % factor == 0):
            num = num / factor
            factor -= 1            
        factor += 1
    return factor


number = 600851475143
print largestPrimeFactor(number)
    
                
            
        
        