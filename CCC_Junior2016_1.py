#Each player in a tournament plays six games. There are no ties. The tournament director places
#the players in groups based on the results of games as follows:
#• if a player wins 5 or 6 games, they are placed in Group 1;
#• if a player wins 3 or 4 games, they are placed in Group 2;
#• if a player wins 1 or 2 games, they are placed in Group 3;
#• if a player does not win any games, they are eliminated from the tournament.
#Write a program to determine which group a player is placed in

group = 0
wins = 0


def grouping():

    if wins >= 5:
        group = 1
        return group

    elif wins >= 3:
        group = 2
        return group

    elif wins >= 1:
        group = 3
        return group

    else:
        group = -1
        return group

for x in range(6):
    match = input("")
    if match == "W":
        wins = wins + 1

    elif match == "L":
        wins = wins



group = grouping()
print(group)