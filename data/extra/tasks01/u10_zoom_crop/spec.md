# zoom_crop

Applies crop and zoom commands to a character grid.

Input: the grid is the lines before the first empty line (rows of equal width). The lines after it are commands, one per line (blank command lines skipped):
- `crop R C H W`: keep the H rows and W columns whose top-left cell is at row R, column C (counted from 0). All four are non-negative integers, H and W at least 1, and the rectangle must lie inside the current grid.
- `zoom K`: K is an integer from 1 to 9; every cell becomes a K by K block of the same character.
- `shrink K`: K from 1 to 9; keeps every K-th cell (rows 0, K, 2K, ... and columns 0, K, 2K, ...).
Any command that is not of these forms, or breaks a rule above (including a crop outside the grid or on an empty grid), prints `error: line N: bad command` where N is its 1-based line number in the whole input, and nothing else is printed.

Output: the final grid, one row per line, followed by `size HxW` (rows by columns; `size 0x0` for an empty grid, and then no rows).

Example input:
```
ab
cd

zoom 2
crop 1 1 2 3
```
Output:
```
abb
cdd
size 2x3
```
Zoom gives `aabb/aabb/ccdd/ccdd`, then the crop starting at row 1, column 1 keeps 2 rows of 3 columns.
