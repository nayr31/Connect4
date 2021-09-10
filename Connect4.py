import BoardManip as board

# Game vars, these determine when the game ends and who plays when
game_over = False
player_turn = True

## Main game loop
while not game_over:
    ## Print the board every time so we can see what happened
    board.printBoard()

    ## Decide who goes when
    if player_turn:
        print("Player turn.")
        board.dropPiece(True)
    else:
        print("AI Turn.")
        board.dropPiece(False)
    
    ## Piece dropped, check for a winner
    received_point = board.check_for_four()
    if received_point == [-99, -99]:
        # Show results first
        board.printBoard()
        game_over = True
        print("Tie.")
    elif not received_point == [-1, -1]:
        board.printBoard()
        ## This funky ternary knows who won by the founded 4 string of pieces
        print("Player " if board.val_at(received_point) == 2 else "AI" + "has won.")
        game_over = True

    ## No winner, toggle turn
    player_turn = not player_turn

print("\nGame Over.")

exit(0)