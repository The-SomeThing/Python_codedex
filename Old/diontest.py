import random

steps = random.randint(4, 10)

hor = 2
ver = 2


min_y = 0
min_x = 0

max_y = 5
max_x = 5

while steps != 0:
    print("What would you like to do? ")
    i = input("> ").lower().strip()
    if i == "move north":
        ver += 1
        print("vertical:",ver," horizontal:", hor)
        
    elif i == "move west":
        hor -= 1
        print("vertical:",ver," horizontal:", hor)

    elif i == "move east":
        hor += 1
        print("vertical:",ver," horizontal:", hor)

    elif i == "move south":
        ver -= 1
        print("vertical:",ver," horizontal:", hor)


    if hor == max_x or hor == min_x:
        print("A great wall stands before you, you cannot move into this direction any further")

    if ver == 2 and hor == 1:
        print("You see a chest, what would ")
        if i == "open":
            print("You found your dignity.")