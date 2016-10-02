#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
#  can see that the 6th prime is 13.
#  What is the 10 001st prime number?


def getPrime(num):
    '''
    return the frist num prime
    '''
    prms = [2]
    num_i = 1
    while (len(prms) < num):
        num_i += 1
        for j in prms:
            if num_i % j == 0:
                break
        else:
            #  print num_i
            prms.append(num_i)
    return num_i

num = 10001  # change here
print getPrime(num)
