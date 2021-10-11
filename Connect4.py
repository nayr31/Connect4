import BoardManip as board

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

    # No winner, toggle turn
    board.player_turn = not board.player_turn

print("\nGame Over.")

board.print_moves()

exit(0)