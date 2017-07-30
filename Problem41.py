#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

from math import *

def pandigital(number):

    number = str(number)
    length = len(number)

    list_1 = []
    for x in range(1, length+1):
        list_1.append(x)

    list_2 = []
    for x in number:
        new_var = int(x)
        list_2.append(new_var)



    if set(list_1) <= set(list_2):
        return True

    else:
        return False


array = []
for x in range(1, 100000001):
    array.append(True)

#sieve algo taken from the wiki page of Sieve of Eratosthenes
def sieve(n):

    for i in range(2, int(sqrt(n))):

        if array[i] == True:

            for j in range((i*i) , n, i):
                array[j] = False


sieve(100000000)

new_array = [i for i, x in enumerate(array) if x == True]
print(new_array)

list_3 = []

for x in new_array:
    if pandigital(x) == True:
        print("oh yeah")
        list_3.append(x)

    print(x)

list_3.sort()
number = len(list_3)

print(list_3[number-1])