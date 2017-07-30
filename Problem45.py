def triangle(n):
    number = (n*(n+1)) / 2
    return number

def pentagon(n):
    number = (n*(3*n-1)) /2
    return number

def hexagonal(n):
    number = (n*(2*n-1))
    return number


x = 285
tri_set = []
pen_set = []
hex_set = []
list_1 = []

tri_set = set(tri_set)
pen_set = set(pen_set)
hex_set = set(hex_set)

while True:
    number_1 = triangle(x)
    number_2 = pentagon(x)
    number_3 = hexagonal(x)

    tri_set.add(number_1)
    pen_set.add(number_2)
    hex_set.add(number_3)

    if tri_set.intersection(pen_set) and tri_set.intersection(hex_set):
        number = triangle(x)
        if number in tri_set:
            if number in hex_set:
                if number in pen_set:
                    print(x, number)
                    break

    print(x)
    x += 1


