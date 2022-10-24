import time
import keyboard
import os
import random


def clear():
    return os.system('cls')


def snake_position(size_board):
    row = random.randrange(3, size_board - 3)
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


# TODO : fix functionality  for tail on the snake

# def adding_tail(the_snake, move, the_board):
#     start_from = 0
#
#     old = the_snake[start_from]
#
#     if len(the_snake) == 1:
#         if move == 'up':
#             the_snake.append((old[0] + 1, old[1]))
#
#         elif move == 'down':
#             the_snake.append((old[0] - 1, old[1]))
#
#         elif move == 'left':
#             the_snake.append((old[0], old[1] + 1))
#
#         elif move == 'right':
#             the_snake.append((old[0], old[1] - 1))
#
#     for _ in the_snake:
#         start_from += 1
#         the_board[old[0]][old[1]] = '*'
#
#     return the_snake, the_board


def move_action(board, row, col, the_move, firs_moves, size):


    board[row][col] = '.'
    row, col = row + firs_moves[the_move][0], col + firs_moves[the_move][1]

    if board[row][col] == 'A':
        apple_row, apple_col = apple_position(size)
        board[row][col] = '*'
        board[apple_row][apple_col] = 'A'
    else:
        board[row][col] = '*'

    return board, row, col



def the_game(board, size):
    snake_row, snake_col = snake_position(size)

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

    apple_row, apple_col = apple_position(size)
    board[apple_row][apple_col] = 'A'

    snake = [(snake_row, snake_col)]


    while True:

        time.sleep(0.20)
        clear()

        if keyboard.is_pressed('down'):
            if move != 'up':
                move = 'down'

                board, snake_row, snake_col = move_action(board, snake_row, snake_col, move, firs_moves, size)


        elif keyboard.is_pressed('right'):
            if move != 'left':
                move = 'right'

                board, snake_row, snake_col = move_action(board, snake_row, snake_col, move, firs_moves, size)

        elif keyboard.is_pressed('up'):
            if move != 'down':
                move = 'up'

                board, snake_row, snake_col = move_action(board, snake_row, snake_col, move, firs_moves, size)

        elif keyboard.is_pressed('left'):
            if move != 'right':
                move = 'left'

                board, snake_row, snake_col = move_action(board, snake_row, snake_col, move, firs_moves, size)

        elif keyboard.is_pressed('escape'):
            break

        else:

            board[snake_row][snake_col] = '.'
            snake_row, snake_col = snake_row + firs_moves[move][0], snake_col + firs_moves[move][1]
            snake[0] = (snake_row, snake_col)

            if 0 < snake_row < len(board) and 0 < snake_col < len(board):
                if board[snake_row][snake_col] == 'A':
                    apple_row, apple_col = apple_position(size)
                    board[snake_row][snake_col] = '*'
                    board[apple_row][apple_col] = 'A'

                    # snake, board = adding_tail(snake, move, board)

                else:
                    board[snake_row][snake_col] = '*'
            else:
                board[snake_row - firs_moves[move][0]][snake_col - firs_moves[move][1]] = '*'
                print('\n\t\tYou dead\n')
                break


        print_board(board)

    print_board(board)


def play_the_game_again(board, size):

    play_again = input('\nDo you wanna play again (yes, no) ?\n')

    if play_again.lower() == 'yes':
        the_game(board, size)

    elif play_again.lower() == 'no':
        print('\nGoodbye')
        time.sleep(1)
        os.system('exit')

def start_the_game(board, size):
    start_game = input('Start game (yes, no) ?\n')

    if start_game.lower() == 'yes':
        the_game(board, size)
        play_the_game_again(board, size)

    elif start_game.lower() == 'no':
        print('\nGoodbye')
        time.sleep(1)
        os.system('exit')



SIZE = 20
board = [['.'] * SIZE for _ in range(SIZE)]

start_the_game(board, SIZE)