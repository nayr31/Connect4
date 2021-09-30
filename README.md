# Connect 4 AI Project

This project aims to create the game "Connect 4", adding an AI as the opponent using minimax as it's basis.

## File details

Below are short descriptions of the purpose of each file in this project.

- `README.md`
  - What you are reading now :)
- `Connect4.py`
  - The main file to run the code from. 
  - Purpose: To have a simple to look at overview of what steps the code is taking from a user perspective.
- `BoardManip.py`
  - Stores the information and definitions required to run the game. Specifically, stores the board object and functions related to manipulating and delegating the information on it.
  - Purpose: To separate the main bulk of the heavy lifting to clean and organize the code.
- `PVector.py`
  - A new object meant to store move data.
  - What is a move?
    - A move is defined by location and the token that was used on that move.
  - Purpose: To simplify the tracking process between depths of minimax.