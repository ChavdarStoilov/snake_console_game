import random

firs_moves = {
    'right': [0, 1],
    'left': [0, -1],
    'down': [1, 0],
    'up': [-1, 0]
}


start_to = random.choice(list(firs_moves.values()))

key_list = list(firs_moves.keys())
val_list = list(firs_moves.values())

position = val_list.index(start_to)
print(key_list[position])