



with open('names2.txt', 'r') as myfile:
    names=myfile.readline( )

names = names.lower()
names = names.split('","')

names[0] = 'a'
names[1785] = "youth"
names.sort()


def triangle_sequence(x):
    term = (x*(x+1)) / 2
    return int(term)


list_1 = []

for x in range(1, 182):
    number = triangle_sequence(x)
    list_1.append(number)

def string_to_number(string):
    sum_of_word = 0
    for x in string:
        number = ord(x)
        number = number - 96
        sum_of_word = sum_of_word + number
    return sum_of_word

sum = 0

for x in names:
    number = string_to_number(x)
    if number in list_1:
        sum += 1


print(sum)