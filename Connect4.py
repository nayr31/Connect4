import BoardManip as board

print("Connect 4 AI Test\nBy Ryan Epp")

board.get_depth()

print("\nStarting game with ai level " + str(board.brain_depth))

# Main game loop
while not board.game_over:
    # Print the board every time so we can see what happened
    board.printBoard()

    # Decide who goes when
    if board.player_turn:
        print("Player turn.")
        board.take_player_turn()
    else:
        print("AI Turn.")
        board.take_ai_turn()
    
    board.check_four_winner() # Yes, the name is a joke

    # Toggle turn every loop
    board.player_turn = not board.player_turn

    # End of loop, if board.game_over changed then it won't run again (check_four_winner does that)

print("\nGame Over.")

exit(0)