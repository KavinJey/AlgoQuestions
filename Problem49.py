#prime permutations

from math import *

array = []
for x in range(1, 10000):
    array.append(True)

#sieve algo taken from the wiki page of Sieve of Eratosthenes
def sieve(n):

    for i in range(2, int(sqrt(n))):

        if array[i] == True:

            for j in range((i*i) , n, i):
                array[j] = False


def comm_diff(term_1, term_2, term_3):
    if term_1 < term_2 < term_3:

        if (term_2 - term_1) == (term_3 - term_2):
            return True

        else:
            return False

    else:
        return False

def check_perms(term_1, term_2, term_3):

    term_1 = str(term_1)
    term_2 = str(term_2)
    term_3 = str(term_3)


    if term_1 != term_2 or term_2 != term_3:

        if set(term_1) <= set(term_2) and set(term_1) >= set(term_2):
            if set(term_2) <= set(term_3) and set(term_2) >= set(term_3):
                if set(term_3) <= set(term_1) and set(term_3) >= set(term_3):

                    return True

        else:
            return False


sieve(9999)

new_array = [i for i, x in enumerate(array) if x == True]
new_list = []

for x in new_array:
    if x > 1000:
        new_list.append(x)





x1 = 0
x2 = 0
x3 = 0
for x in range(1060):

    x1 += 1
    term_1 = new_list[x1]
    print(term_1)

    while x < 1061:
        x2 += 1
        if x2 >= len(new_list):
            x2 = 0
            break

        term_2 = new_list[x2]
        print(term_1, term_2)


        while x < 1060:

            if x3 >= len(new_list):
                x3 = 0
                break

            term_3 = new_list[x3]
            print(term_1, term_2, term_3)

            if check_perms(term_1, term_2, term_3) == True:
                if comm_diff(term_1, term_2, term_3) == True:
                    print(term_1, term_2, term_3, "\n\n\nOH YEAH BUDDY")
                    value_1 = term_1
                    value_2 = term_2
                    value_3 = term_3

            x3 += 1


print(value_1, value_2, value_3)



