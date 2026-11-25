# sudoku_easy

Reads one 9x9 sudoku grid from standard input and prints its solution.

## Input
Exactly 9 non-empty lines (after trimming), each exactly 9 characters: a digit `1`-`9` for a given cell or `.` for an empty cell. Blank lines are ignored.

## Output
- If the input is not 9 lines of 9 valid characters, print `invalid input`.
- If the given digits already repeat inside a row, a column or a 3x3 box, or the grid cannot be completed, print `no solution`.
- Otherwise print the 9 lines of the completed grid. When several solutions exist, print the one found by filling empty cells in row-major order, trying digits 1 to 9 in increasing order.

## Example
Input (a grid with one empty cell):
```
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
34528617.
```
Output:
```
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```
