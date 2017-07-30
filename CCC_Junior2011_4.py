coordinates = []

for x in range(401):
    for y in range(201):
        coordinates.append((x,y))

if (0,1) in coordinates:
    coordinates.pop()
    print(coordinates)