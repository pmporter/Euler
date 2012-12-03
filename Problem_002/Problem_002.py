'''
Created on Dec 3, 2012

@author: pporter5
'''
class Problem002:
    '''
    By considering the terms in the Fibonacci sequence whose values 
    do not exceed four million (4,000,000), find the sum of the 
    even valued terms
    '''

    def __init__(self, upperBound = 4000000):
        '''
        Constructor
        '''
        self.upperBound = upperBound
        self.sum = self.__calculate(self.upperBound)
        
    def __calculate(self,upperBound):
        '''
        '''
        sum = 0
        fib = 0
        helper = 0
        while helper < upperBound:
            sum +=1
        
        return sum
        
        
if __name__ == '__main__':
    solution = Problem002(4000000)