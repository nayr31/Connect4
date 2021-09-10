import random

# Constants
width, height = 7, 6
top_string = " 0 1 2 3 4 5 6"

# Board information and setup
## I ended up using a 1 for an empty space, 2 for a player space, and 0 for an AI space
## Yes it is dumb
board = []
for i in range(height):
    board.append(list(range(width)))
for i in range(height):
    for j in range(width):
        board[i][j] = 1
#last_place = [-1, -1]

# Prints the board according to the example given:
##  0 1 2 3 4 5 6
## | | | | | | | |
## | | | | | | | |
## | |X|O| | | | |
## | |O|X|X| | | |
## | |O|X|O| | | |
## |X|O|O|O|X| | |
## The spots in the board are converted using the ternary operation
## Why not just store the board like this? Because reasons.
def printBoard():
    print(top_string)
    for row in board:
        ## Always starts empty ""
        build_string = ""
        for spot in row:
            ## So that every iteration we put the left wall and its contents "|X"
            build_string += "|"
            #print("Checking spot: " + str(spot))
            build_string +=  "X" if str(spot) == "2" else " " if str(spot) == "1" else "0"
        ## Ending with the capstone "|X|O|""
        build_string += "|"
        print(build_string)

# Confirms that there is an open space at the top of the board. If there is, then it can't be full.
def is_valid_drop(column):
    # First, check if its inside the range of our bounds
    if column > width-1 or column < 0:
        print("Selected column is too " + "high" if column > width-1 else + "low" + ". Try again.")
        return False
    # Then we can check for column validity
    # Check the top most row (board[0]) for a 1
    ## A "1" indicates an empty space, meaning we can place something there
    if board[0][column] != 1:
        print("Column is full! Try another.")
        return False
    ## Yes this could have just returned board[0][column] == 1, but I wanted error specific messages
    return True

# Places a piece at the selected column, and assumes that it can (will throw an error if it can't, but that shouldn't happen)
def place_piece(selection, token):
    ## Got the selected column, need to find the lowest point
    lowest_point = -1

    ## Iterate through each of the 6 rows (i) and find the "lowest" box without a "1"
    for i in range(height):
        if board[i][selection] == 1:
            lowest_point = i

    ## Lowest point found, set the token
    board[lowest_point][selection] = token
    #last_place = [lowest_point, selection]
    print("Dropped token into column [" + str(selection) + "]")

# A stupidly named method, this actually is the "take turn" method
# Basically depending on which turn it is the program will do whatever it needs to for that player
def dropPiece(is_player):
    selection = -1

    if is_player:
        ## Get the column the player wants to drop into, making sure its valid
        while True:
            # Error handling is handled inside of the is_valid method
            selection = int(input("Which column to drop into?: "))
            if is_valid_drop(selection):
                break

        place_piece(selection, 2)
        ## Done the player's turn
    else:
        ## AI mumbo jumbo
        print("Beep bop, I am a robot.")

        while True:
            ## Look for a suitable column
            selection = random.randint(0,6)

            ## Check that it works
            if is_valid_drop(selection):
                place_piece(selection, 0)
                break

def check_for_four():
    ## Check in each direction for a connection, limited by the width/height of the board
    
    ## Horizontal
    ### In the below, we only start on the [x] and look right (instead of looking both left and right). The 3 is for the required space for a 4 pair
    ### Ill omit the preamble from the coming ones.
    ### [x] [o] [o] [o] 
    ### [x] [o] [o] [o] 
    ### [x] [o] [o] [o] 
    ### [x] [o] [o] [o]
    #print("Checking horizontal")
    for row in range(height):
        for column in range(width - 3):
            if board[row][column] == board[row][column + 1]\
                == board[row][column + 2] == board[row][column + 3]\
                    and not board[row][column] == 1:
                return [row, column]
    
    ## Vertical
    ### [x] [x] [x] [x] (only looking downwards)
    ### [o] [o] [o] [o] 
    ### [o] [o] [o] [o] 
    ### [o] [o] [o] [o]
    #print("Checking vertical")
    for row in range(height - 3):
        for column in range(width):
            if board[row][column] == board[row + 1][column]\
                == board[row + 2][column] == board[row + 3][column]\
                and not board[row][column] == 1:
                return [row, column]

    ## Diagonal down (left to right)
    ### [x] [o] [o] [o] (only one valid point here)
    ### [o] [o] [o] [o] 
    ### [o] [o] [o] [o] 
    ### [o] [o] [o] [o]
    #print("Checking ltr")
    for row in range(height - 3):
        for column in range(width - 3):
            if board[row][column] == board[row + 1][column + 1]\
                == board[row + 2][column + 2] == board[row + 3][column + 3]\
                and not board[row][column] == 1:
                return [row, column]

    ## Diagonal up (left to right)
    ## It doesn't need to look diagonally right to left downwards, cause that would be the same thing
    ### [o] [o] [o] [o] (looking at it going up instead of like before)
    ### [o] [o] [o] [o] 
    ### [o] [o] [o] [o] 
    ### [x] [o] [o] [o]
    #print("Checking rtl")
    ## This range here starts at the bottom (height - 1)
    for row in range(height - 1, height - 3, -1): # start at the bottom, search upwards (since we are getting cut off at the top)
        for column in range(width - 3):
            #print("point : " + str(row) + str(column))
            if board[row][column] == board[row - 1][column + 1]\
                == board[row - 2][column + 2] == board[row - 3][column + 3]\
                and not board[row][column] == 1:
                return [row, column]

    ## Not connections, but the board could be full (making a tie)
    is_full = True
    for row in range(height):
        for column in range(width):
            if board[row][column] == 1:
                is_full = False
                break

    if is_full:
        return [-99, -99]
    
    return [-1, -1]

# Returns the value on the board when given a point (list of two numbers)
def val_at(point):
    return board[point[0], point[1]]
