t_1 = int(input())
t_2 = int(input())

sequence = []
sequence.append(t_1)
sequence.append(t_2)


for x in range(10001):

    new_term = (t_1 - t_2)


    if t_2 < new_term:
        sequence.append(new_term)
        break

    sequence.append(new_term)
    t_2 = new_term
    t_1 = sequence[x+1]



print(len(sequence))
