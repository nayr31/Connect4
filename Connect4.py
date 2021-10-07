import BoardManip as board

## Main game loop
while not board.game_over:
    ## Print the board every time so we can see what happened
    board.printBoard()

    ## Decide who goes when
    if board.player_turn:
        print("Player turn.")
        board.take_turn(True)
    else:
        print("AI Turn.")
        board.take_turn(False)
    
    # Piece dropped, check for a winner
    # This process is a mess and could be improved
    received_point = board.check_for_four()
    #print(received_point)
    if received_point == [-99, -99]:
        # Show results first
        board.printBoard()
        board.game_over = True
        print("Tie.")
    elif not received_point == [-1, -1]:
        board.printBoard()
        ## This funky ternary knows who won by the founded 4 string of pieces (if there are no moves, then someone cheated!)
        print(("Player " if board.moves[-1].data == 2 else "AI ") + "has won.")
        board.game_over = True

    ## No winner, toggle turn
    board.player_turn = not board.player_turn

print("\nGame Over.")

exit(0)