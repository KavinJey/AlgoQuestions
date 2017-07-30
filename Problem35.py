from math import *

array = []

for x in range(1, 1001):
    array.append(True)

#GOOD PERMUTATION ALGO
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def sieve(n):
    for i in range(2, int(sqrt(n))):
        if array[i] == True:
            for j in range((i*i) , n, i):
                array[j] = False

sieve(1000)

new_array = [i for i, x in enumerate(array) if x == True]
new_array.remove(0)
new_array.remove(1)

circular_prime_list = []

#make permutations check for every combo to be prime
def circular_prime(n):
    number = str(n)
    list_2 = []
    condition = False

    for x in number:
        list_2.append(x)

    new_list = []

    #Reason this doesn't work is because cyclic rotation does not mean permutation
    for p in all_perms(list_2):
        p = int(''.join(p))

        new_list.append(p)

    print(n, new_list)

    if set(new_array) >= set(new_list):
        condition = True


    if condition == True:
        if p in new_array:
            circular_prime_list.append(n)



for x in new_array:
    circular_prime(x)


print(len(new_array), len(circular_prime_list))
print(circular_prime_list)