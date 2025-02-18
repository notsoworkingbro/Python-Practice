# Create a 10 by 7 map 
#          10 rows 7 columns

# the game randomly picks 3 bonus squares, it picks different squares
# the game randomly picks only 5 out of 7 columns
# and after picking the 5 columns it will pick a square from 1 to 10th row in that particular column

# the player is alowwed to pick any square before the game starts, the goal is pick the square that will be randomly selected by the game the (which is either 1 or 4 in the output game_map)
# if the player correctly picked the square wich is equal to 1 he wins
# if the player luckily picked the bonus square which is 4 he wins bonus prizes

# bonus squares occurs when the random square from the 5 out of 7 columns 
# and after the game picking the 5 columns it will pick a square from 1 to 10th row in that particular column also lands the bonus square (3) 
# and be picked by the player in the same time

#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+
#                             |0|0|0|0|0|0|0|
#                             +-+-+-+-+-+-+-+

import random

game_map = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

row_list = [0, 1, 2, 3, 4, 5, 6]

unlucky_random_col_numbers = random.sample(range(0, 6), 2)
random_bonus_row =           random.sample(range(0, 9), 3)
random_bonus_col =           random.sample(range(0, 6), 3)

# Remove the selected column numbers from the row
# filtered_row = [value for index, value in enumerate(row_list) if index not in unlucky_random_col_numbers]

filtered_row = []

for x in row_list:
    if x not in unlucky_random_col_numbers:
        filtered_row.append(x)

print("fltrd",filtered_row)

for x in range(0, 3):
    game_map[random_bonus_row[x]][random_bonus_col[x]] = 3

for x in filtered_row:
    random_row = random.randint(0, 9)
    if game_map[random_row][x] == 3:
       game_map[random_row][x] = 4

    else:
        game_map[random_row][x] = 1
        

for x in range(len(game_map)):
    print(f"{game_map[x]}")
