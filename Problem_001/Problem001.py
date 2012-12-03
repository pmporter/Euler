'''
Created on Dec 3, 2012

@author: pporter5
'''

class Problem001:
    '''
    Add all the natural numbers below 1000 that are
    multiples of 3 or 5.
    '''


    def __init__(self,upperBound=1000):
        '''
        Constructor
        '''
        self.upperBound = upperBound
        self.sum = self.__calculate(self.upperBound)
        
    def __calculate(self,upperBound):
        sum = 0
        for i in range(self.upperBound):
            if (i % 5 == 0) or (i % 3 == 0):
                sum += i
        return sum
        
                
if __name__ == "__main__":
    solution = Problem001(1000)
    print "The sum of all natural numbers below " + str(solution.upperBound) + " is " + str(solution.sum)
       
                
                
                
                
                
                
                
                
                
                
                
                
                
            
        
        