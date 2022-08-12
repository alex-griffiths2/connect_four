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
                return True
    
    # Check for vertical row of 4 winning move
    for row in range(len(board)-3):
        for col in range(len(board[row])):
            if board[row,col] == board[row+1,col] and board[row,col] == board[row+2,col] and board[row,col] == board[row+1,col] and board[row,col] == player:
                return True

    # Check for positive slope of 4 winning move
    for row in range(0,4):
        for col in range(4,len(board[row])):    
            if board[row,col] == board[row+1,col-1] and board[row,col] == board[row+2,col-2] and board[row,col] == board[row+3,col-3] and board[row,col] == player:
                return True

    # Check for negative slope of 4 winning move
    for row in range(0,4):
        for col in range(0,4):    
            if board[row,col] == board[row+1,col+1] and board[row,col] == board[row+2,col+2] and board[row,col] == board[row+3,col+3] and board[row,col] == player:
                return True

def token_drop(player,board,selection):
    for row in len(ROW_COUNT):
        # If the slot is empty and the next slot is taken (not equal to zero), then place the token here (equal to the players' number)
        if board[selection,row] == 0 and board[selection,(row+1)] != 0
            board[selection,row] == player

# Check if the player has selected a valid move
def valid_move(selection):
    if board[selection,0] == 0 and selection > 0 and selection < 7:
        return True
    else
        return False

# Playing the game
while not winning_move == True:
    # define player 1's turn
    if turn%2 == 0:     
        selection = int(input("Player 1, please select a column to place your token"))
        
        # Keep asking for user input if they make incorrect selections
        while valid_move(selection) == False:
            print("Invalid move, please try again")
            selection = int(input("Player 1, please select a column to place your token"))
        
        token_drop(player_1,board,selection)
        winning_move(player_1)
        print(board)
        turn += 1
    
    elif not turn%2 == 0:
        selection = int(input("Player 2, please select a column to place your token"))
        
        # Keep asking for user input if they make incorrect selections
        while valid_move(selection) == False:
            print("Invalid move, please try again")
            selection = int(input("Player 2, please select a column to place your token"))
        
        token_drop(player_2,board,selection) 
        winning_move(player_2)
        print(board)
        turn += 1









