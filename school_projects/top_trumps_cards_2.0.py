import random

title = ['Name: ' , 'Distance from Sun: ' , 'Size: ' , 'Orbital Period: ' , 'Number of Moons']

cards = [
['Mercury', 57.9, 4879, 88, 0],
['Venus', 108.2, 12104, 224.7, 0],
['Earth', 149.6, 12756, 365.2, 1],
['Mars', 227.9, 6792, 687, 2],
['Jupiter', 778.6, 142984, 4331, 67],
['Saturn', 1433.5, 120536, 10747, 62],
['Uranus', 2872.5, 51118, 30589, 27],
['Neptune', 4495.1, 49528, 59800, 14], ]

human_cards = [
['Mercury', 57.9, 4879, 88, 0],
['Venus', 108.2, 12104, 224.7, 0],
['Earth', 149.6, 12756, 365.2, 1],
['Mars', 227.9, 6792, 687, 2],
['Jupiter', 778.6, 142984, 4331, 67],
['Saturn', 1433.5, 120536, 10747, 62],
['Uranus', 2872.5, 51118, 30589, 27],
['Neptune', 4495.1, 49528, 59800, 14],]

computer_cards = [
['Mercury', 57.9, 4879, 88, 0],
['Venus', 108.2, 12104, 224.7, 0],
['Earth', 149.6, 12756, 365.2, 1],
['Mars', 227.9, 6792, 687, 2],
['Jupiter', 778.6, 142984, 4331, 67],
['Saturn', 1433.5, 120536, 10747, 62],
['Uranus', 2872.5, 51118, 30589, 27],
['Neptune', 4495.1, 49528, 59800, 14],]

def pc(c) :
    print("_________________________________")
    print(' ')
    print(title[0] + str(c[0]))
    print(title[1] + str(c[1]))
    print(title[2] + str(c[2]))
    print(title[3] + str(c[3]))
    print(title[4] + str(c[4]))

x = 0 
y = int((7-x)*random.random())
pc(human_cards[y])

z = input('choose attribute: ')

y = int((7-x)*random.random())
pc(computer_cards[y])

