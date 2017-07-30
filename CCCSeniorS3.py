dict = {1: 0, 2: 0, 3: 0, 4: 0}
games_played = {1: 0, 2: 0, 3: 0, 4: 0}

team = int(input().strip())

n = int(input().strip())

for x in range(n):
    scores = input().split()
    scores = list(map(int, scores))
    if scores[2] > scores[3]:
        dict[scores[0]] += 3
        games_played[scores[0]] += 1

    elif scores[3] > scores[2] :
        dict[scores[1]] += 3
        games_played[scores[1]] += 1

    else:
        dict[scores[0]] += 1
        dict[scores[1]] += 1
        games_played[scores[0]] += 1
        games_played[scores[1]] += 1


for x in range(6-n):
    for