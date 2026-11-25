# Connect four winner

Standard input: each line is one game on a board of 7 columns and 6 rows, given as the columns played, in order, written as digits `1` to `7` with no separators.
Players alternate, R (red) first and then Y (yellow). A piece dropped in a column falls to the lowest free row.
A player wins by having four of their pieces in a straight line (horizontal, vertical or diagonal) in a row.

For each line print one verdict:
- `R wins at move N` or `Y wins at move N`: the move number N (counting from 1) that completed four in a row. No move may follow it.
- `draw`: all 42 cells are filled and nobody has four in a row.
- `in progress`: no winner yet, the board is not full, and the line has no problem (an empty line is `in progress`).
- `invalid`: a character that is not a digit 1-7, a move into a full column, or any move after the game has been won (checked as the moves are read, in order).

A final newline does not add a game; empty input prints nothing.

Example:
    input:  4433221
            1212121
            44
    output: R wins at move 7
            R wins at move 7
            in progress
