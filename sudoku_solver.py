
sudoku_board = [
    [0, 1, 0],
    [0, 3, 2],
    [0, 0, 1],
]

# Back tracker
def nextCell(board, row, column):
    max = len(board);
    
    for x in range(row, max):
        for y in range(column, max):
            if board[x][y] == 0:
                    return x,y
                    
    for x in range(0, max):
        for y in range(0, max):
            if board[x][y] == 0:
                    return x,y
    
    return -1,-1

# Element validator
def isValid(board, row, column, element):
    max = len(board);
    
    # Check elements with in the same row
    if board[row].count(element) > 0:
        return False
    
    # Check elements with in the same column
    col_values = [board[i][column] for i in range(max)]
    if(col_values.count(element) > 0):
        return False
    
    return True
        

# Boards solver
def solve(board, row = 0, column = 0):
    row, column = nextCell(board, row, column)
    max = len(board);
    
    if row == -1:
        return True
    
    for element in range(1, max + 1):
       if isValid(board, row, column, element):
            board[row][column] = element
           
            if solve(board, row, column):
                return board
            
            # Undo the current cell for backtracking
            board[row][column] = 0
           
    return False
        


# Solve sudoku
solved = solve(sudoku_board)
if(solved):
    for row in solved:
        print(row)
else:
    print("Can't be solve !!")
    