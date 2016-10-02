
## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def getPrime(num):
    '''
    produce prims smaller than num
    '''
    for num_i in xrange(1, num+1):
        if num_i!=1:
            for j in xrange(2, (num_i//2)):
                if num_i%j==0:
                    break
            else:
                yield num_i

def commonMultiple(num1, num2):
    '''
    retun a low common multiple bewteen num1 and num2
    '''
    rem=[num1, num2]
    prms=getPrime(min(rem))

    # collect cofactors
    cofactors={}
    for factor in prms:
        count=0
        while True:
            r1, r2= rem[0]%factor, rem[1]%factor
            if r1==0 and r2==0:
                count+=1
                rem[0], rem[1]= rem[0]/factor, rem[1]/factor
            else:
                break
        if count>0:
            cofactors[factor]=count

    # multiple cofactors
    product=1
    for f in cofactors:
        product=product* f ** cofactors[f]
    # multiple reminders
    for f in rem:
        product = product * f

    return product

num=20
multiple=1

for i in xrange(1, num+1):
    multiple=commonMultiple(multiple, i)

print multiple

