import time
import keyboard
import os
import random


def clear():
    return os.system('cls')


def snake_position(size_board):
    row = random.randrange(0, size_board)
    col = row

    return row, col


def print_board(board):
    print(' #' * (len(board) + 1))
    for the_board in board:
        print(f"# {' '.join(the_board)} #")
    print(' #' * (len(board) + 1))


def apple_position(size_board):

    row = random.randrange(0, size_board)
    col = row

    return row, col


def the_game():
    SIZE = 20
    board = [['.'] * SIZE for _ in range(SIZE)]

    snake_row, snake_col = snake_position(SIZE)

    firs_moves = {
        'right': (0, 1),
        'left': (0, -1),
        'down': (1, 0),
        'up': (-1, 0)
    }

    start_to = random.choice(list(firs_moves.values()))

    key_list = list(firs_moves.keys())
    val_list = list(firs_moves.values())

    move = key_list[val_list.index(start_to)]

    snake_row, snake_col = snake_row + start_to[0], snake_col + start_to[1]

    apple_row, apple_col = apple_position(SIZE)
    board[apple_row][apple_col] = 'A'
    snake = []


    while True:
        time.sleep(0.20)
        clear()

        if keyboard.is_pressed('s'):
            move = 'down'
            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            board[snake_row][snake_col] = 'S'

        elif keyboard.is_pressed('d'):
            move = 'right'
            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            board[snake_row][snake_col] = 'S'

        elif keyboard.is_pressed('w'):
            move = 'up'
            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            board[snake_row][snake_col] = 'S'

        elif keyboard.is_pressed('a'):
            move = 'left'
            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            board[snake_row][snake_col] = 'S'

        elif keyboard.is_pressed('escape'):
            break
        else:
            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            if 0 < snake_row < len(board) and 0 < snake_col < len(board):
                board[snake_row][snake_col] = 'S'
            else:
                board[snake_row - firs_moves[move][0]][snake_col - firs_moves[move][1]] = 'S'
                print('\nYou dead\n')
                break


        print_board(board)

    print_board(board)


def play_the_game_again():

    play_again = input('\nDo you wanna play again (yes, no) ?\n')

    if play_again.lower() == 'yes':
        the_game()
    elif play_again.lower() == 'no':
        print('\nGoodbye')
        time.sleep(1)
        os.system('exit')

def start_the_game():
    start_game = input('Start game (yes, no) ?\n')

    if start_game.lower() == 'yes':
        the_game()
        play_the_game_again()
    elif start_game.lower() == 'no':
        print('\nGoodbye')
        time.sleep(1)
        os.system('exit')


start_the_game()

