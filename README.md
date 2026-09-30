# Tic Tac Toe

## Project Overview

Tic Tac Toe is a simple two-player game developed using Python. The game is played on a 3 x 3 board through the terminal.

Players take turns choosing positions from 1 to 9. The program checks the move, updates the board and checks for a winner or a draw.

## Features

- Two-player gameplay
- 3 x 3 board
- Player X and Player O
- Input validation
- Prevention of repeated positions
- Win detection
- Draw detection
- Score tracking
- Replay option

## Technology Used

- Python 3
- Python lists
- Functions
- Loops
- Conditional statements

No external libraries are required.

## Project File

The complete game is written in one Python file:

`tic_tac_toe.py`

The program contains functions for displaying the board, checking winning combinations, validating player positions, running the game and maintaining the score.

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python tic_tac_toe.py
```

4. Enter a position from 1 to 9 when asked.
5. Follow the instructions shown in the terminal.

## Example Board

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Testing

The program can be tested manually by:
- Entering a valid position.
- Entering a letter instead of a number.
- Entering a number outside 1 to 9.
- Selecting an occupied position.
- Completing a winning row, column or diagonal.
- Filling the board without a winner to test a draw.
- Playing multiple rounds to check the score.

## Future Improvements

- Add a single-player mode.
- Add a computer opponent.
- Add a graphical interface.
- Save scores between program runs.
