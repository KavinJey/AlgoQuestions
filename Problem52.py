#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def numbers(n):
    list_of_numbers = []
    list_of_numbers.append(str(n))
    list_of_numbers.append(str(2*n))
    list_of_numbers.append(str(3*n))
    list_of_numbers.append(str(4*n))
    list_of_numbers.append(str(5*n))
    list_of_numbers.append(str(6*n))

    return list_of_numbers


condition = True
number = 1

while condition == True:

    list_1 = numbers(number)
    for x in range(len(list_1)-1):
        if set(list_1[0]) >= set(list_1[1]):
            if set(list_1[1]) >= set(list_1[2]):
                if set(list_1[2]) >= set(list_1[3]):
                    if set(list_1[3]) >= set(list_1[4]):
                        condition = False





    number += 1

print(number)