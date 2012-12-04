'''
Add all the natural numbers below 1000 that are
multiples of 3 or 5.
'''
sum = 0
upperBound = 1000

for i in range(upperBound):
    if (i % 5 == 0) or (i % 3 == 0):
        sum += i

print 'The sum of all natural numbers below ' + str(upperBound) + ' that are multiples of 3 or 5 is: ' + str(sum)