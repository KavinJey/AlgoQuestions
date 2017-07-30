#pentagonal numbers

import math

def pentagon(n):
    number = (n*(3*n-1)) /2
    return number

x = 1
list_1 = []

while True:

    number = pentagon(x)
    list_1.append(number)
    print(number)
    x += 1

    if len(list_1) > 10000:
        break



new_list = []
check = set(list_1)

for q in list_1:

    for z in list_1:

        difference = abs(q - z)
        sum = q + z
        if difference in check:
            if sum in check:
                table_2 = [z, q]
                new_list.append(table_2)



    print(q, z)



print(new_list)