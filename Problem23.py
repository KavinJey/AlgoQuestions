#Non-abundant sums upper limit 28123
#number is abundant if it's proper divisors are more than the number itself
#number is deficient if all proper divisors are less than the number itself

#great algo kavin great job
#perfect divisor function that returns list of divisors

#NEED TO FIND NUMBERS THAT CANNOT BE THE SUM OF TWO ABUNDANT NUMBERS
def perfect_divisors(n):
    list_1 = []
    condition = True
    start = 1
    stop = 9

    while condition == True:
        for x in range(start, stop):
            #adds perfect divisors to list
            if n % x == 0:
                list_1.append(x)

            #stops the program if x is greater than n
            if x > n/2:
                condition = False
                break


        start = stop - 1
        stop = stop + 10


    list_1 = set(list_1)

    return list_1

#checking if number is abundant or not
def abun_defCond(n):
    if sum(perfect_divisors(n)) > n:
        return True

    else:
        return False

new_list = []

for q in range(1, 28124):

    if abun_defCond(q):
        new_list.append(q)
    print(q, len(new_list))

new_list.remove(2)
new_list = set(new_list)

def arithmetic(n, x):
    number = n - x
    return abs(number)




list_2 = []

for z in range(12, 28124):
    for x in new_list:
        check = arithmetic(z, x)
        if check in new_list:
            list_2.append(z)
            break

        else:
            break

    print(z)

list_3 = []
for x in range(1, 28124):
    list_3.append(x)

list_3 = set(list_3)
list_2 = set(list_2)

list_3 = list_3 - list_2

print(list_3, "\n", sum(list_3))
print(new_list)