# Tic-tac-toe judge

Standard input: each line is one game on a 3x3 board. The board cells are numbered 0 to 8 (row by row, 0 is top-left, 8 is bottom-right).
A line holds the cells played, separated by spaces, in order. X moves first and the players alternate.

For every line print exactly one verdict:
- `X wins` or `O wins` when that player completes a row, column or diagonal and no moves follow it.
- `draw` when all 9 cells are filled and nobody has won.
- `in progress` when the game is not decided and the line has fewer than 9 moves (an empty line is `in progress`).
- `invalid` when any token is not an integer from 0 to 8, a cell is played twice, or any move comes after the game was already won.

Lines are separated by newlines; every line (even an empty one) is one game. A final newline does not add a game. Empty input prints nothing.

Example:
    input:  0 3 1 4 2
            4 0 8 1 5 2 3 6 7
    output: X wins
            draw
