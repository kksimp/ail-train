# nonogram_row

Checks filled rows of a nonogram puzzle against their clues.

## Input
One check per line (blank lines ignored, lines trimmed): `CLUES ROW`, separated by a single space. CLUES is a comma-separated list of positive integers (the lengths of the runs of filled cells, left to right), or `0` for a row with no filled cells. ROW is a string of `#` (filled) and `.` (empty).

## Output
One line per check:
- `ok` if the runs of consecutive `#` in ROW, read left to right, are exactly the clues.
- `bad: got RUNS want CLUES` otherwise, where RUNS and CLUES are the run lengths separated by single spaces (`none` for an empty list).
- `invalid` if the line does not have exactly two fields, ROW has a character other than `#` or `.`, or CLUES contains something other than positive integers (or the single `0`).

## Example
Input:
```
3,1 ###.#..
2 #.#.
0 ....
```
Output:
```
ok
bad: got 1 1 want 2
ok
```
