#  The sum of the squares of the first ten natural numbers is,

#  12 + 22 + ... + 102 = 385
#  The square of the sum of the first ten natural numbers is,

#  (1 + 2 + ... + 10)2 = 552 = 3025
#  Hence the difference between the sum of the squares of the first ten
#  natural numbers and the square of the sum is 3025 - 385 = 2640.

#  Find the difference between the sum of the squares of the first one
#  hundred natural numbers and the square of the sum.

def sqrsum(num):
    '''
    return the sum of the sqares of num
    '''
    res=0
    for i in xrange(1, num+1):
        res=res + (i **2)
    return res

def sumsqr(num):
    '''
    return the squres the sume of num
    '''
    res=sum(range(1, num+1))
    res=res**2
    return res

num=100 #change num
print sumsqr(num)-sqrsum(num)
