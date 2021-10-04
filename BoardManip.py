# This file is for anything that relates to the board. The main program should not know what it needs to do, only what it wants to.
# This could just be my Java seeping into my Python, but this is how I like it.

from PVector import PVector
import random

# Constants
width, height = 7, 6
top_string = "+ 0 1 2 3 4 5 6 "
moves = []
player_token, empty_token, ai_token = 2, 1, 0
lowest_in_column = [5, 5, 5, 5, 5, 5, 5]

# Board information and setup
## I ended up using a 1 for an empty space, 2 for a player space, and 0 for an AI space
## Yes it is dumb, no I am not going to change it
board = []
for i in range(height):
    board.append(list(range(width)))
for i in range(height):
    for j in range(width):
        board[i][j] = empty_token

# Prints the board according to the example given (without the pieces):
##   0 1 2 3 4 5 6
## 0| | | | | | | |
## 1| | | | | | | |
## 2| |X|O| | | | |
## 3| |O|X|X| | | |
## 4| |O|X|O| | | |
## 5|X|O|O|O|X| | |
## The spots in the board are converted using the ternary operation
## Why not just store the board like this? Because reasons.
def printBoard():
    print(top_string)
    imp = -1
    for row in board:
        imp += 1
        ## Always starts empty ""
        build_string = str(imp)
        for spot in row:
            ## So that every iteration we put the left wall and its contents "|X"
            build_string += "|"
            #print("Checking spot: " + str(spot))
            build_string +=  "X" if str(spot) == str(player_token) else " " if str(spot) == str(empty_token) else "0"
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
    ## A "1" indicates an empty space, meaning we can place something there
    if board[0][column] != empty_token:
        print("Column is full! Try another.")
        return False
    ## Yes this could have just returned board[0][column] == 1, but I wanted error specific messages
    return True

# A stupidly named method, this actually is the "take turn" method
# Basically depending on which turn it is the program will do whatever it needs to for that player
# This allows the main runtime to choose how it wants to run the game, while this just takes care of the backend
def take_turn(is_player):
    selection = -1

    if is_player:
        ## Get the column the player wants to drop into, making sure its valid
        while True:
            # Error handling is handled inside of the is_valid method
            selection = int(input("Which column to drop into?: "))
            if is_valid_drop(selection):
                break

        make_move(selection, player_token)
        ## Done the player's turn
    else:
        # AI is supposed to be "Minimax", meaning it looks a certain distance in the future (board states) then chooses the best outcome.
        # Alpha-beta pruning should be used to determine b-tree outcomes that just don't look great and we can ignore.
        #   This will speed up the program by looking at less possibilities, while also reducing memory usage by storing less values.
        #   Maybe higher winning odds as well?
        print("Beep bop, I am a robot.")

        while True:
            ## Look for a suitable column
            selection = random.randint(0,6)

            ## Check that it works
            if is_valid_drop(selection):
                make_move(selection, ai_token)
                break

# Refreshes the lowest known row per column for all columns
def refresh_lowest_all():
    for col in range(width):
        refresh_lowest_at(col)

# Refreshes the entry of the lowest row at a certain column
def refresh_lowest_at(col):
    #print("Refresh col=" + str(col))
    for row in range(height):
        if board[row][col] == empty_token:
            lowest_in_column[col] = row
        else:
            #print("Broke at row=" + str(row))
            break
    #print("Finished entire column.")

# Returns a list of each possible drop point and its respective score to the simple leads
def score_board(token):
    # Generate lowest possible points (just in case)
    #refresh_lowest_all()
    print(lowest_in_column)

    # Search through all columns last empty node to see the potential score of adjacent pieces
    col_score = [-1, -1, -1, -1, -1, -1, -1]
    for i in range(width):
        refresh_lowest_at(i)
        #print("Starting search in col " + str(i) + " for row " + str(lowest_in_column[i]))
        col_score[i] = score_col(token, lowest_in_column[i], i,  0, -1)

    #print("Got best score of " + str(best_score) + " in " + str(best_col))
    return col_score

# Looks around the current location for a given token. If it is, then it will proceed down that path.
# Dir is used to avoid circles because I am bad a coding recursion
## [0] [1]  [2] (1 is unused)
## [7] [-1] [3]
## [6] [5]  [4]
# Desired expansions/TODO:
#   - Have the ai score itself vs the player. This would be in the minimax, but essentially compare the scores of both "placing best for me" and "placing worst for them"
#       - Ideally, we would want both, so after we would want the program to "add" the scores up for finals
def score_col(token, row, column, length, dir):
    #print("Recursion data: [" + str(column) + ", " + str(row) + "], " + str(length) + (", root" if dir is -1 else ""))
    best_len = -1 # Best length of this column, overall score
    
    # Store the initial best score from each direction
    best_score_in_dir = [-1, -1, -1, -1, -1, -1, -1]

    ## Left 3 (up-left, left, down-left)
    if column != 0:
        ## up-left
        if row - 1 >= 0:
            if dir == -1 or dir == 0:
                if board[row - 1][column - 1] == token:
                    best_score_in_dir[0] = score_col(token, row - 1, column - 1, length + 1, 0)
        ## left
        if dir == -1 or dir == 7:
            if board[row][column - 1] == token:
                best_score_in_dir[7] = score_col(token, row, column - 1, length + 1, 7)
        ## down-left
        if row + 1 < height:
            if dir == -1 or dir == 6:
                if board[row + 1][column - 1] == token:
                    best_score_in_dir[6] = score_col(token, row + 1, column - 1, length + 1, 6)

    ## down
    if row + 1 < height:
        if dir == -1 or dir == 5:
            if board[row + 1][column] == token:
                best_score_in_dir[5] = score_col(token, row + 1, column, length + 1, 5)

    ## Right 3 (right-down, right, right-up)
    if column != width-1:
        ## right-down
        if row + 1 < height:
            if dir == -1 or dir == 4:
                if board[row + 1][column + 1] == token:
                    best_score_in_dir[4] = score_col(token, row + 1, column + 1, length + 1, 4)
        ## right
        if dir == -1 or dir == 3:
            if board[row][column + 1] == token:
                best_score_in_dir[3] = score_col(token, row, column + 1, length + 1, 3)
        ## right-up
        if row - 1 >= 0:
            if dir == -1 or dir == 2:
                if board[row - 1][column + 1] == token:
                    best_score_in_dir[2] = score_col(token, row - 1, column + 1, length + 1, 2)
    #print("Got best_val of " + str(best_len) + " from " + str(length) + ", dir:" + str(dir))
    
    # Now we have the best score (common tokens) in each direction, although we want to bridge some as well
    ## [0] = left-down (0 and 4)
    ## [1] = straight right (7 and 3)
    ## [2] = left-up (6 and 2)
    ## [3] = down (down doesn't share a straight)
    # If I set the initial values in the best_in_score_dir to 0, it might break something. Something to improve/investigate if performance is bad
    best_in_common = [-1, -1, -1, best_score_in_dir[5]]
    best_in_common[0] = (best_score_in_dir[0] if best_score_in_dir[0] is not -1 else 0) + (best_score_in_dir[4] if best_score_in_dir[4] is not -1 else 0)
    best_in_common[1] = (best_score_in_dir[7] if best_score_in_dir[7] is not -1 else 0) + (best_score_in_dir[3] if best_score_in_dir[3] is not -1 else 0)
    best_in_common[2] = (best_score_in_dir[6] if best_score_in_dir[6] is not -1 else 0) + (best_score_in_dir[2] if best_score_in_dir[2] is not -1 else 0)
    

    if best_len < length:
        #print("Got end case, BL=" + str(best_len) + ", L=" + str(length) + " at [" + str(column) + ", " + str(row) + "]")
        return length
    #print("Skipped end case, BL=" + str(best_len) + ", L=" + str(length) + " at [" + str(column) + ", " + str(row) + "]")
    return best_len

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
                    and not board[row][column] == empty_token:
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
                and not board[row][column] == empty_token:
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
                and not board[row][column] == empty_token:
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
                and not board[row][column] == empty_token:
                return [row, column]

    ## Not connections, but the board could be full (making a tie)
    is_full = True
    for row in range(height):
        for column in range(width):
            if board[row][column] == empty_token:
                is_full = False
                break

    if is_full:
        return [-99, -99]
    
    return [-1, -1]

# Returns the value on the board when given a point (list of two numbers)
def val_at(point):
    return board[point[0], point[1]]

# Test method; Sets selected coordinates to certain pieces [col, row, token_type]
def test_move():
    make_move(0, player_token)
    make_move(0, player_token)
    make_move(0, player_token)
    make_move(0, player_token)
    make_move(1, player_token)

# Test method; returns the current board score of the player [token_type]
def test_score_player():
    return score_board(player_token)

# The following methods use the concept of a "move".
## A move is defined as the position and piece that was placed.
## The PVector object stores the location and piece data in a single object
# This concept allows us to make and unmake moves easily for recursive tree searching
def make_move(column, token): # This is the one that should be used normally, letting the program take care of the row
    move = PVector(column, lowest_in_column[column], token)
    #print("Making move: x=" + str(move.x) + " y=" + str(move.y) + " data=" + str(move.data))
    moves.append(move)
    board[move.y][move.x] = move.data
    refresh_lowest_at(column)

#def make_move(move): # This is a debug move, made for forcefully setting a selected box to a token
#    moves.append(move)
#    board[move.y][move.x] = move.data

def unmake_move(): # Undo-s the last move made
    move = moves.pop()
    board[move.y][move.x] = empty_token
    refresh_lowest_at(move.x)

def restart():
    moves.clear()
    lowest_in_column