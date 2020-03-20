# single line comment

"""
multiple line comments
"""
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

# print_board(board)

# find empty squares in board
def find_empty(bo):
    for i in range (len(bo)):
        for j in range (len(bo[0]))
            if bo[i][j] == 0:
                return (i, j)   # return indecies (row, column)
                
    return None