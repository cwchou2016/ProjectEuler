# encoding=utf8

##The following iterative sequence is defined for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13, we generate the following sequence:
##
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
##Which starting number, under one million, produces the longest chain?
##
##NOTE: Once the chain starts the terms are allowed to go above one million.


COUNTS={} # Record the counts of each number


def func(n, count=0):
    '''
    return count until n ==1
    '''
    global COUNTS
    if n==1:
        return count+1
    else:
        if n in COUNTS:    # if n has been count, use it
            count += COUNTS[n]
            return count
        elif n%2==0:
            res=n/2
            #print res,
            count=count+1
            return func(res,count)
        else:
            res=3*n +1
            #print res,
            count=count+1
            return func(res, count)        

num=1000000
max_count=0
for nmb in xrange(1, num):
   # print nmb, 
    count=func(nmb)
    COUNTS[nmb]=count # save count of number
    #print count
    if count > max_count:
        theNum=nmb
        max_count=count

print theNum, max_count

