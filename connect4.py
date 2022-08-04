import numpy

# Define global params for number of rows and columns in the matrix
ROW_COUNT = 6
COLUMN_COUNT = 7
Turn = 0
# Create an empty board with 0's
def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))

board = create_board()
board[1,1] = 1
print(board)
def game_over():
    pass

def empty_slot(column):
    pass

def place_token(column):
    if board[column,0] == 0:
        pass

while not game_over:
    if turn % 2 == 0:
        column = int(input("Player 1, please make your column"))
        turn += 1
        place_token(column)
    else:
        column = int(input("Player 2, please make your column"))
        turn += 1
        place_token(column)




