from math import *


array = []
for x in range(1, 1000001):
    array.append(True)

list_2 = []
for x in range(1, 1000001):
    list_2.append(True)

#sieve algo taken from the wiki page of Sieve of Eratosthenes
def sieve(n, array):

    for i in range(2, int(sqrt(n))):

        if array[i] == True:

            for j in range((i*i) , n, i):
                array[j] = False



sieve(1000000, array)
sieve(1000000, list_2)

array = [i for i, x in enumerate(array) if x == True]
list_2 = [i for i, x in enumerate(list_2) if x == True]

list_2.remove(1)
list_2.remove(0)

array.remove(1)
array.remove(0)


check = set(list_2)
value = 0

for x in list_2:
    sum = 0
    count = 0
    for q in range(list_2.index(x)):
        sum += x
        count += 1
        if sum in check:

            if count > value:
                value = count
                number = sum

        else:
            break

    print(x)

print(value, number)

