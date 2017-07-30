#a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100

a = 2

numbers = []
number = 0

while a < 101:
    b = 2
    for x in range(2, 101):
        print(a, b)
        number = a**b
        b += 1
        numbers.append(number)

    a += 1



numbers = list(set(numbers))
numbers.sort()


print(numbers)
print(len(numbers))