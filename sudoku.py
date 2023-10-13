def isValid(grid, row, column, k):
    notInRow = k not in grid[row]
    notInColumn = k not in [grid[i][column] for i in range(9)]
    notInBox = k not in [grid[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in range(column // 3 * 3, column // 3 * 3 + 3)]
    return notInRow and notInColumn and notInBox

def solveSud(grid, row=0, column=0):
    if row == 9:
        return True
    elif column == 9:  
        return solveSud(grid, row + 1, 0)
    elif grid[row][column] != 0:
        return solveSud(grid, row, column + 1)
    else:
        for k in range(1, 10):
            if isValid(grid, row, column, k):
                grid[row][column] = k
                if solveSud(grid, row, column + 1):
                    return True
                grid[row][column] = 0
        return False

sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solveSud(sudoku_grid):
    print("Solved Sudoku:")
    for row in sudoku_grid:
        print(row)
else:
    print("No solution found.")
