# Connect 4 AI Project

This project aims to create the game "Connect 4", adding an AI as the opponent using minimax as it's basis.

Made and tested with [Python 3.9.6](https://www.python.org/downloads/release/python-396/) in [VSCode](https://code.visualstudio.com).

You can find the link to the [GitHub repo here](https://github.com/nayr31/Connect4), if you found this project otherwise.

## Usage

Make sure you have the entire project extracted from the `.zip` you downloaded it from before continuing.

In any python compiler, run the `Connect4.py` file.

## Personal Analysis

### AI flaws

- Will drop into a space that cannot under any circumstance become a four in a row
  - If there is a space of 1 in between two pieces (to make a straight of 2, going to 3), then it will drop it if it is the best move, even if there are no other means of making a straight (going above 3) on either side
  - Example: [X] [0] [ ] [0] [X]
- Sometimes will just let the player win???
  - I really have no idea with this one on why it is happening.
- The evaluation is quite poor, right now these are the steps it takes:
  - For each column, find the following score:
    - Connected pieces of the same type in each direction
    - Allows skipping on empty spaces, but not player spaces
    - Combines the common cartesian (left-right, left-top-right-bottom, etc.)
    - Return the best score
  - Return the best score of those columns

### Performance

Minimax takes around 1 second at a depth of 5, and around 7 seconds at a depth of 6.

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
