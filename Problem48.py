#self-powers
number = 0

for x in range(1, 1001):
    number = number + x**x

number = str(number)
length = len(number)

for z in range(1,11):
    print(number[length - z])
