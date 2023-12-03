import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    for row in board:
        print(" ".join(map(str, row)))

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def move(board, direction):
    for i in range(4):
        row = board[i]
        row = [tile for tile in row if tile != 0]
        if direction == 'left':
            row = merge_left(row)
        elif direction == 'right':
            row = merge_right(row)
        row += [0] * (4 - len(row))
        board[i] = row

    transpose_board(board) if direction in ['up', 'down'] else None
    return board

def merge_left(row):
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return [tile for tile in row if tile != 0]

def merge_right(row):
    return [tile for tile in row[::-1] if tile != 0][::-1]

def transpose_board(board):
    board[:] = [list(row) for row in zip(*board)]

def is_game_over(board):
    return all(tile != 0 for row in board for tile in row) and \
           not any(row[i] == row[i + 1] or (row[i] == 0 or row[i + 1] == 0) for row in board for i in range(3))

def is_win(board):
    return any(tile == 2048 for row in board for tile in row)

def main():
    board = initialize_board()
    print_board(board)

    while True:
        direction = input("Enter direction (up, down, left, right) or 'q' to quit: ").lower()

        if direction == 'q':
            print("Quitting the game. Thanks for playing!")
            break

        if direction in ['up', 'down', 'left', 'right']:
            board = move(board, direction)
            add_random_tile(board)
            print_board(board)

            if is_win(board):
                print("Congratulations! You won!")
                break

            if is_game_over(board):
                print("Game over! Try again.")
                break

if __name__ == "__main__":
    main()
