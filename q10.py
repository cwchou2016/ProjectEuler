#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#  Find the sum of all the primes below two million.

num=2000000

sqrn=num**(1/2.0)
prms=range(2,num)

idx=0

while (idx < len(prms)):
    base= prms[idx]
    #  print base
    if base**2 >= num:
        break
    else:
        mtpls=set(range(base*2, num, base))
        prms=[n for n in prms if n not in mtpls]
    idx+=1

print sum(prms)
