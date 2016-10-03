
## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
## a2 + b2 = c2
## For example, 32 + 42 = 9 + 16 = 25 = 52.
##
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

def findb(a,num):
    '''
    a^2 + b^2 =C^2
    a+b+c =num
    return b of the Pythagorean triplet
    
    '''
    b= ((num**2)/2.0 - (num*a))/(num-a)
    return b

def findc(a,b):
    """
    return c of the Pythagorean triplet
    """
    c= (a**2 + b**2)**(1/2.0)
    return c

num=1000 # change here

qt=num/4.0

for i in range(1,(int(qt+1))):
    b= findb(i, num)
    if b%1==0:
      a=i
      break

p=a * b* findc(a,b)

print p
