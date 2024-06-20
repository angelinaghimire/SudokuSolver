import time

def is_valid_move(matrix, row, col, num):
    # Check if the number 'num' can be placed at position (row, col) in the matrix
    for x in range(9):
        if matrix[row][x] == num:
            return False
    for x in range(9):
        if matrix[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if matrix[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty_location(matrix):
    # Find the next empty location in the matrix
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                return row, col
    return -1, -1

def solve(matrix):
    # Solve Sudoku recursively
    row, col = find_empty_location(matrix)
    if row == -1:
        return True  # Puzzle solved
    for num in range(1, 10):
        if is_valid_move(matrix, row, col, num):
            matrix[row][col] = num
            if solve(matrix):
                return True
            matrix[row][col] = 0  # Backtrack
    return False

def print_sudoku(matrix):
    # Print the Sudoku grid
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end=" ")
        print()
        