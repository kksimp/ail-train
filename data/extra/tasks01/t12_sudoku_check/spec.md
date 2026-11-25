# Sudoku grid validator

Reads one 9x9 sudoku grid and says whether it breaks the rules so far.

Input: the grid, 9 lines of 9 characters each, where a character is a digit `1`-`9` or `.` for an empty cell. Empty lines and surrounding whitespace on a line are ignored. If, after that, there are not exactly 9 lines, or any line is not exactly 9 valid characters, print `BAD INPUT`.

Rules: no digit may appear twice in a row, in a column, or in a 3x3 box. Check, in this order: all rows (top to bottom), then all columns (left to right), then all boxes (numbered 1-9 in reading order, cells read row by row). Inside one unit, read its cells in order and stop at the first cell whose digit already appeared earlier in that unit.

Output, one line:
- `INVALID row R digit D` / `INVALID column C digit D` / `INVALID box B digit D` for the first conflict found (R, C, B are 1-based).
- Otherwise `VALID complete` if there are no `.` cells, else `VALID incomplete`.

Example input (a conflict of two 5s in row 1):
```
5.5......
.........
.........
.........
.........
.........
.........
.........
.........
```
Example output:
```
INVALID row 1 digit 5
```

Empty input prints `BAD INPUT`.
