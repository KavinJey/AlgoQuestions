# Collatz Sequence
# Finding number that produced longest chain under one million

def odd(x):
    x = 3 * (x) + 1
    return x


def even(x):
    x = x / 2
    return x

sequence_count = 0

for x in range(1, 1000001):

    sequence = []
    integer = x

    while integer != 1:

        if integer % 2 == 0:
            number = even(integer)
            sequence.append(number)


        elif integer % 2 != 0:
            number = odd(integer)
            sequence.append(number)

        integer = number


    if sequence_count < len(sequence):
        sequence_count = len(sequence)
        start_number = x

    print(x)

print(sequence_count, start_number)