# color game gambling
# there are 6 colors to bet in
# 3 dices will fall, the dice's faces will be corresponding to the 6 colors
# when the 3 dices lands we will see their faces up, the number of color that will appear will be treated as a multiplier
# example when dice1: blue, dice2: blue, dice3: red (2x for blue) (1x for red)

import random

dices = {
    "dice1" : random.randint(0, 5),
    "dice2" : random.randint(0, 5),
    "dice3" : random.randint(0, 5)
    }

colors = {
    "Red" :     0,
    "Blue" :    1,
    "Green" :   2,
    "Yellow" :  3,
    "Purple" :  4,
    "Orange" :  5,
}

# assume 1 
random_choice = random.randint(0, 5)

multiplier = 0

for value in dices:
    x = dices[value]
    print(x)
    # if random_choice == x:
    #     # multiplier += 1
    #     # print(multiplier)
        

for value in colors:
    x = colors[value]
    # print(x)