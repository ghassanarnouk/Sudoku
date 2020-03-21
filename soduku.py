# board is an array of 9 elements. Each element is another array of 9 elements
board = [
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

# solve the board using recursion 
def solve(bo):
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

# check if sudoku rules are applied
def valid(bo, num, pos):
    # check row
    for i in range (len(bo[0])):
        # 
        if bo[pos[0]][i] == num and pos[1] != i:    # bo[row][col]
            return False

    # check columns
    for i in range (len(bo[0])):
        # 
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3     # returns 0, 1, or 2 representing horizontal boxes
    box_y = pos[0] // 3     # returns 0, 1, or 2 representing vertical boxes

    for i in range (box_y*3, box_x*3 + 3):
        for j in range (box_x*3, box_y*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# print sudoku board
def print_board(bo):
    for i in range (len(bo)):   # len(bo) returns the number of elements in array
        # To format sudoku horizontally
        if i%3 == 0 and i != 0:     # i!=0: a line isn't printed at the beginning
            print("-----------------------")

        for j in range (len(bo[0])):    # len(bo[0]) returns the number of elements in array
            # To format sudoku vertically
            if j%3 == 0 and j != 0:
                print(" | ", end = "")  # end = "": won't go to a new line after printing

            # print board
            if j == len(bo[0]) - 1:
                # new line printed if last element     
                print(bo[i][j])     
            else:
                # print elements next in rows 
                print(str(bo[i][j]) + " ", end = "")    # str(): converts number into string     

# find empty squares in board
def find_empty(bo):
    for i in range (len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)   # return indecies (row, column)
                
    return None

print_board(board)
solve(board)
print ("\n*************************\n*************************\n")
print_board(board)