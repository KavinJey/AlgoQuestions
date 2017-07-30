#QUADRATIC PRIMES

def quadratic(n, a, b):

    formula = n**2 + a*n + b
    return formula


def check_prime(n):
    if n <= 1:
        return False

    elif n <= 3:
        return True

    elif n % 2 == 0  or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6

    return True


condition = True
n = 0
list_2 = []
new_list = []

while condition == True:

    for x in range(-1000, 1001):
        a = x

        for b in range(-1000, 1001):

            number = quadratic(n, a, b)

            n += 1
            print(number, x, b, n)
            if check_prime(number) == True:

                list_2.append(number)

                value_1 = x
                value_2 = b
                print(len(list_2))

                if len(list_2) >= len(new_list):
                    new_list = list_2
                    condition = False
                    break





        list_2 = []
        n = 0

print(len(new_list))
print(value_1, value_2)
print(value_1*value_2)