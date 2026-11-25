Read a maze from standard input: lines of equal length made of the characters `#` (wall), `.` (open), `S` (start) and `E` (end).
Blank lines are ignored. A move is one step up, down, left or right onto a cell that is not a wall; no diagonals, and no leaving the grid.
The input has at most one `S` and at most one `E`.

Print the minimum number of steps from `S` to `E` as a single integer.
If `E` cannot be reached, print `no path`.
If there is no `S` or no `E` (this includes empty input), print `invalid`.

Example input:
```
S.#
..#
#.E
```
Output:
```
4
```
