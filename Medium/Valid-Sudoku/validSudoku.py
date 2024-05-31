class Solution:
    def isValidSudoku(board) -> bool:
        # Check Columns
        for x in range(9):
            foundNum = [False,False,False,False,False,False,False,False,False]
            for y in range(9):
                if board[x][y] != ".":
                    whichNum = int(board[x][y])
                    if foundNum[whichNum-1] == True:
                        return False
                    foundNum[whichNum-1] = True
        # Check Rows
        for y in range(9):
            foundNum = [False,False,False,False,False,False,False,False,False]
            for x in range(9):
                if board[x][y] != ".":
                    whichNum = int(board[x][y])
                    if foundNum[whichNum-1] == True:
                        return False
                    foundNum[whichNum-1] = True
        # Check Boxes
        # Make a string from the values of each square in a box. Then count characters of string for duplicates.
        for i in range(3):
            for j in range(3):
                square = board[0+(i*3)][0+(j*3)] + board[1+(i*3)][0+(j*3)] + board[2+(i*3)][0+(j*3)] + \
                         board[0+(i*3)][1+(j*3)] + board[1+(i*3)][1+(j*3)] + board[2+(i*3)][1+(j*3)] + \
                         board[0+(i*3)][2+(j*3)] + board[1+(i*3)][2+(j*3)] + board[2+(i*3)][2+(j*3)]
                for x in range(9):
                    if square.count(str(x+1)) > 1:
                        return False
        return True