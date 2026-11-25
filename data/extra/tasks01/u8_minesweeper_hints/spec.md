# minesweeper_hints

Reads a minefield and prints the hint grid.

## Input
One or more lines (blank lines ignored, each line trimmed), all the same length, made only of `*` (a mine) and `.` (a safe cell).

## Output
The same grid where every `*` stays `*` and every `.` becomes the number (0 to 8) of mines among its up to 8 neighbours.
- If the lines differ in length or contain any other character, print only `invalid field`.
- Empty input prints nothing.
- After the grid print a line `mines: M` with the total number of mines, but only when the field is valid and non-empty.

## Example
Input:
```
*..
...
.*.
```
Output:
```
*10
222
1*1
mines: 2
```
