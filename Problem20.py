 #Factorial sum

from math import *
factorial(2)

number = factorial(100)

number = str(number)
number_list = []

for x in number:
    integer = int(x)
    number_list.append(integer)



print(number_list)
print(sum(number_list))