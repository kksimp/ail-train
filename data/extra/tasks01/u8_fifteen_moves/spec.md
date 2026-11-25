# fifteen_moves

Validates and applies a sequence of moves on a 15-puzzle (4x4 sliding tiles).

## Input
Four lines, each holding four integers separated by single spaces: the board, where `0` is the blank. The fifth line is the move string (it may be missing or empty). Each move character moves the blank: `U` up, `D` down, `L` left, `R` right (the neighbouring tile slides into the blank's place).

## Output
- If the board lines are not four lines of four integers that together are exactly 0..15 once each, print `invalid board` and stop.
- Apply the moves in order. If a move would take the blank off the board, print `illegal move K` (K is the 1-based position of the move in the string) and stop. If a character is not one of `UDLR`, print `bad move K` and stop.
- Otherwise print the final board as four lines (tiles separated by single spaces), then `solved` if the board is 1 2 ... 15 followed by 0, else `unsolved`.

## Example
Input:
```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 0 15
R
```
Output:
```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0
solved
```
