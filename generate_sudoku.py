import initialize_board
import random
import is_valid_move

def generate_sudoku():
    board = initialize_board()
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid_move(board, row, col, num):
            board[row][col] = num
    return board

