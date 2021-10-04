import BoardManip as board

# Game vars, these determine when the game ends and who plays when
game_over = False
player_turn = True

## Main game loop
while not game_over:
    ## Print the board every time so we can see what happened
    board.test_move()
    board.printBoard()
    print("Test scores: " + str(board.test_score_player()))

    ## Decide who goes when
    if player_turn:
        print("Player turn.")
        board.take_turn(True)
    else:
        print("AI Turn.")
        board.take_turn(False)
    
    ## Piece dropped, check for a winner
    # This process is a mess and could be improved
    received_point = board.check_for_four()
    if received_point == [-99, -99]:
        # Show results first
        board.printBoard()
        game_over = True
        print("Tie.")
    elif not received_point == [-1, -1]:
        board.printBoard()
        ## This funky ternary knows who won by the founded 4 string of pieces (if there are no moves, then someone cheated!)
        print(("Player " if board.moves[-1].data == 2 else "AI") + "has won.")
        game_over = True

    ## No winner, toggle turn
    player_turn = not player_turn

print("\nGame Over.")

exit(0)