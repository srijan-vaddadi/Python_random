import random

cards = [
['Mercury', 57.9, 4879, 88, 0],
['Venus', 108.2, 12104, 224.7, 0],
['Earth', 149.6, 12756, 365.2, 1],
['Mars', 227.9, 6792, 687, 2],
['Jupiter', 778.6, 142984, 4331, 67],
['Saturn', 1433.5, 120536, 10747, 62],
['Uranus', 2872.5, 51118, 30589, 27],
['Neptune', 4495.1, 49528, 59800, 14],
['Pluto', 5906.4, 2370, 90560, 5] ]

def pc(c) :
    print("_________________________________")
    print(' ')
    print('Name: ' + str(c[0]))
    print('Distance from Sun: ' + str(c[1]))
    print('Size: ' + str(c[2]))
    print('Orbital Period: ' + str(c[3]))
    print('Number of Moons: ' + str(c[4]))

x = 0
while x < len(cards):
    y = int((8-x)*random.random())
    pc(cards[y])
    cards[y] = cards[8-x]
    x = x + 1