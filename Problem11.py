#Summation of Primes
#Find sum of rprimes below two million


#Finding sum of prime numbers under two million


#Borrowed algorithm

from math import *

def primes_sieve2(limit):


    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False



#My attempt



#sieve algo taken from the wiki page of Sieve of Eratosthenes
def sieve(n):
    array = []
    for x in range(1, n + 1):
        array.append(True)

    for i in range(2, int(sqrt(n))):
        if array[i] == True:
            for j in range((i*i) , n, i):
                array[j] = False

    array = [i for i, x in enumerate(array) if x == True]
    array.remove(0)
    array.remove(1)

    return array

array = sieve(2000000)



print(new_array)

#holy shit it fucking works
#but why
