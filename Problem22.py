
#turns string to numbers


with open('names.txt', 'r') as myfile:
    names=myfile.readline( )

names = names.lower()
names = names.split('","')

names[0] = 'mary'
names[5162] = "alonso"
names.sort()

product = 0

for x in names:
    integer = names.index(x) + 1
    product = product + (string_to_number(x) * integer)




print(product)

