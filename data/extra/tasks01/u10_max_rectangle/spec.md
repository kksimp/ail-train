# max_rectangle

Finds the largest axis-aligned rectangle made only of `1` cells in a binary grid.

Input: non-empty lines of `0` and `1` characters, all the same width (empty lines are ignored). A line with any other character makes the whole input invalid: print `error: bad grid` and nothing else.

Output: if there is at least one `1`, a single line `area A at R,C size HxW`, where the rectangle has height H, width W, area A = H*W, and its top-left cell is at row R, column C (both counted from 0). If several rectangles have the largest area, pick the one with the smallest R, then the smallest C, then the smallest H. If there is no `1` (or the input is empty) print `area 0`.

Example input:
```
10100
10111
11111
10010
```
Output:
```
area 6 at 1,2 size 2x3
```
