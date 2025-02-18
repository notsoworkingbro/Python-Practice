# Goofy aaahh methods
# turning game_map values into a desired number

def badmapping():
    game_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    for y in range(len(game_map)):

        # 0 - 4 depends on how long are the arrays inside the array of game_map
        # turning each row (y) into 1s [1, 1, 1, 1, 1]

        game_map[y][0] = 1
        game_map[y][1] = 1
        game_map[y][2] = 1
        game_map[y][3] = 1
        game_map[y][4] = 1

    print(f"{game_map} Bad Mapping 0")

def badmapping1():
    game_map = []

    # assume the arrays inside game_map is fixed
    # placing arrays inside an array
    x = [1, 1, 1, 1, 1]

    # range depends on how many arrays user wants inside the game_map
    for y in range(5):
        game_map.append(x)

    print(f"{game_map} Bad Mapping 1")

def mapping():
    game_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # create new map flattened the 3d map
    # flattened map is dictioary

    flattened_map = {}

    x_limit = len(game_map[0])             # indicates the limit of the array insied the game_map
    y_limit = len(game_map)                # indicates the limit of game_map
    
    x = 0
    y = 0

    while x < x_limit and y < y_limit:
        flattened_map[f"{x}-{y}"] = 1      # assigns  x-y as key and 5 the value --> 0-0 : 1
        x += 1                             # increments the variable till it hits the limit 
        if x == 5:                         # after x variable hits the limit set x to 0 again and increment y
            x = 0
            y += 1
    
    # this turns each value to 1 per column

    # '0-0': 1, 
    # '1-0': 1, 
    # '2-0': 1, 
    # '3-0': 1, 
    # '4-0': 1, 

    # '0-1': 1, 
    # '1-1': 1, 
    # '2-1': 1, 
    # '3-1': 11, 
    # '4-1': 1, 

    # '0-2': 1, 
    # '1-2': 1, 
    # '2-2': 1, 
    # '3-2': 1, 
    # '4-2': 1, 

    # '0-3': 1, 
    # '1-3': 1, 
    # '2-3': 1, 
    # '3-3': 1, 
    # '4-3': 1, 

    # '0-4': 1, 
    # '1-4': 1, 
    # '2-4': 1, 
    # '3-4': 1, 
    # '4-4': 1
    print(f"{flattened_map} Mapping")



    # a = [5, 5, 5, 5, 5]
    # game_map = [a for x in range(5)]
    # print(game_map)

def mapping1():
    game_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # get length of the game_map
    y = len(next(iter(game_map)))

    for i in range(len(game_map) * y):

        # solution for row
        row = int(i / len(game_map))

        # solution for col
        col = int(i % len(game_map))

        # get exact point and change its value
        game_map[row][col] = 1

    # issue is only works with perfect squares
    print(f"{game_map} Mapping1")

def mapping2():
    game_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # Get the number of columns (y) from the first row
    y = len(next(iter(game_map)))

    # Iterate over the entire grid (number of rows * columns)
    for i in range(len(game_map) * y):
        row = i // y  # Calculate row index
        col = i % y   # Calculate column index

        game_map[row][col] = 1

    # Print the updated game_map
    print(f"{game_map} Mapping 2")

# 00
# 01
# 02
# 03
# 04

# 10
# 11
# 12
# 13
# 14

# 20
# 21
# 22
# 23
# 24

# 30
# 31
# 32
# 33
# 34

# 40
# 41
# 42
# 43
# 44

badmapping()
badmapping1() 
mapping()
mapping1()
mapping2()