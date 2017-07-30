#max weight of bridge
W = int(input().strip())

#Amount of trains
T = int(input().strip())

trains = []
for x in range(T):
    trainWeight = int(input().strip())
    trains.append(trainWeight)


n = 0
first_train = 0
last_train = 4

while n != len(trains):

    if sum(trains[first_train:last_train]) > W:
        print(last_train-1)
        break

    else:

        n += 1
        last_train += 1
        first_train += 1



