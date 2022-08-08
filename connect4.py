import numpy

# Define global params for number of rows and columns in the matrix
ROW_COUNT = 6
COLUMN_COUNT = 7
turn = 0
player = 1

# Create an empty board with 0's and store in the variable 'board'
def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))
board = create_board()

def winning_move():

    # Check for horizontal row of 4 winning move
    for col in len(COLUMN_COUNT): 
        for row in len(ROW_COUNT):
            if (board[col])

            elif 

    # Check for vertical row of 4 winning move
    # Check for positive slope winning move
    # Check for negative slope winning move
def token_drop(player,board,selection):
    for row in len(ROW_COUNT):
        # If the slot is empty and the next slot is taken (not equal to zero), then place the token here (equal to the players' number)
        if board[selection,row] == 0 and board[selection,(row+1)] != 0
            board[selection,row] == player
        

def valid_move(selection):
    if board[selection,0] == 0:
        return True
    else
        return False

while not game_over:
    if turn % 2 == 0:
        selection = int(input("Player 1, please make your selection"))
        player = 1
        turn += 1
        place_token(selection)
    else:
        selection = int(input("Player 2, please make your selection"))
        pLayer = 2
        turn += 1
        place_token(selection)






