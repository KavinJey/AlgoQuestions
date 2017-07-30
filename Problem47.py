from math import *

#Prime Factorization
def findPrimes(n):
    listPrimes = []
    while (n%2 == 0):
        listPrimes.append(2)
        n = n/ 2

    for x in range(3, int(sqrt(n))+1, 2):
        while (n%x == 0):
            listPrimes.append(int(x))
            n = n / x

    if (n > 2):
        listPrimes.append(int(n))


    return listPrimes

x = 999

num = 0
while True:
    numbers = []
    for x in range(x, x+5):
        factors = findPrimes(x)
        factors = list(set(factors))

        if len(factors) == 4:
            for b in range(len(factors)):
                if factors.count(b) > 1:
                    break

            numbers.append(x)


            if len(numbers) == 4:
                if numbers[0] + 1 == numbers[1] and numbers[1] + 1 == numbers[2] and numbers[2] + 1 == numbers[3]:
                    print(numbers)
                    break

        else:

            break


    x += 1


