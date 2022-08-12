from distutils.log import error
import numpy


# Define global params for number of rows and columns in the matrix
ROW_COUNT = 7
COLUMN_COUNT = 7
turn = 0

player_1 = input("Choose one of the following symbols ! @ # $ % ^ & * + as your connect 4 piece \n")
player_2 = input("Choose one of the following symbols ! @ # $ % ^ & * + as your connect 4 piece \n")

# Define player names
player_1 = input("Please enter Player 1's name \n")
player_2 = input("Please enter Player 2's name \n")

# Create an empty board with 0's and store in the variable 'board'
def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))
board = create_board()
board[1,2] = 1
print(board)


def winning_move(player):
    # Check for horizontal row of 4 winning move
    for row in range(len(board)):
        for col in range(len(board[row])-3):
            if board[row,col] == board[row,col+1] and board[row,col] == board[row,col+2] and board[row,col] == board[row,col+3] and board[row,col] == player:
                return "Player {player_name} wins!!".format(player_name=player)
    
    # Check for vertical row of 4 winning move
    for row in range(len(board)-3):
        for col in range(len(board[row])):
            if board[row,col] == board[row+1,col] and board[row,col] == board[row+2,col] and board[row,col] == board[row+1,col] and board[row,col] == player:
                return "Player {player_name} wins!!".format(player_name=player)

for i in row_:
    fefsef


    # Check for positive slope of 4 winning move
    for row in range(0,4):
        for col in range(4,len(board[row])):    
            if board[row,col] == board[row+1,col-1] and board[row,col] == board[row+2,col-2] and board[row,col] == board[row+3,col-3] and board[row,col] == player:
                return "Player {player_name} wins!!".format(player_name=player)

    # Check for negative slope of 4 winning move
    for row in range(0,4):
        for col in range(0,4):    
            if board[row,col] == board[row+1,col+1] and board[row,col] == board[row+2,col+2] and board[row,col] == board[row+3,col+3] and board[row,col] == player:
                return "Player {player_name} wins!!".format(player_name=player)

def token_drop(player,board,selection):
    for row in len(ROW_COUNT):
        # If the slot is empty and the next slot is taken (not equal to zero), then place the token here (equal to the players' number)
        if board[selection,row] == 0 and board[selection,(row+1)] != 0
            board[selection,row] == player


# def valid_move(selection):
#     if board[selection,0] == 0:
#         return True
#     else
#         return False

# while not game_over:
#     if turn % 2 == 0:
#         selection = int(input("Player 1, please make your selection"))
#         player = 1
#         turn += 1
#         place_token(selection)
#     else:
#         selection = int(input("Player 2, please make your selection"))
#         pLayer = 2
#         turn += 1
#         place_token(selection)






