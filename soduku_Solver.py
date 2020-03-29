# A backtracking program in Python to solve Sudoku problem

# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and 3x3 boxes)
def solve_sudoku(board):
    # find an unassigned location
    find = find_empty_location(board)

    if find:
        # assign indecies of an unassigned location
        row, col = find
    else:
        # no empty locations are available 
        return True

    # attempt to place digits 1-9 in the cell which fulfill the criteria
    for i in range(1, 10):
        # check if digit is valid
        if valid(board, i, (row, col)):
            board[row][col] = i

            # recursively move to the next cell and try to fill it, if possible
            if solve_sudoku(board):
                # return true when board is solved
                return True
            
            # reset the current cell that was just filled
            board[row][col] = 0
    # no solution found
    return False

# Function to check whether it is valid to assign num to the given row,col.
# returns a boolean which indicates whether it is valid to assign 
# num to the given row,col location.
def valid(board, number, position):
    # check row
    for i in range (len(board[0])):
        # returns a boolean which indicates whether any assigned entry
        # in the specified row matches the given number.
        # 'position[1] == i' is the location of the unassigned cell we are trying to fill in row.
        if board[position[0]][i] == number and position[1] != i:    # board[row][col]
            return False

    # check column
    for i in range (len(board[0])):
        # returns a boolean which indicates whether any assigned entry
        # in the specified column matches the given number.
        # 'position[1] == i' is the location of the unassigned cell we are trying to fill in column.
        if board[i][position[1]] == number and position[0] != i:    # board[row][col]
            return False

    # returns a boolean which indicates whether any assigned entry
    # within the specified 3x3 box matches the given number;
    box_x = position[1] // 3     # returns 0, 1, or 2 representing horizontal boxes
    box_y = position[0] // 3     # returns 0, 1, or 2 representing vertical boxes

    for i in range (box_y*3, box_x*3 + 3):
        for j in range (box_x*3, box_y*3 + 3):
            # '(i, j))== position' is the location of the unassigned cell we are trying to fill in 3x3 box.
            if board[i][j] == number and (i, j) != position:
                return False

    return True

# A utility function to print the grid
def print_grid(board):
    for i in range (len(board)):   # len(board) returns the number of elements in array
        # To format sudoku horizontally
        if i%3 == 0 and i != 0:     # i!=0: a line isn't printed at the beginning
            print("-----------------------")

        for j in range (len(board[0])):    # len(board[0]) returns the number of elements in array
            # To format sudoku vertically
            if j%3 == 0 and j != 0:
                print(" | ", end = "")  # end = "": won't go to a new line after printing

            # print grid
            if j == len(board[0]) - 1:
                # print new line if last element     
                print(board[i][j])     
            else:
                # print elements next in rows 
                print(str(board[i][j]) + " ", end = "")    # str(): converts number into string     

# Function to find the entry in the grid that is still not used
# searches the grid to find an entry that is still unassigned.
# if found, the reference parameters i, j (row, col) will set the location
# that is unassigned, and are returned.
# if no unassigned entries remain, None is returned.
def find_empty_location(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == 0:
                # return (row, column)
                return (i, j)   
    # there is no such return value            
    return None 

# Main function
if __name__ == '__main__':
    # Creating a 2D array for the grid
    grid = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]    

    # if success, print the grid
    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("No solution exists!")