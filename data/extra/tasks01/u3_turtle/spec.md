# turtle: drawing on a character grid

A turtle draws on a grid of 12 columns and 6 rows. Position (x, y): x = column 0..11 from the left, y = row 0..5 from
the top. It starts at (0, 0) heading east (E) with the pen down, and the start cell is already drawn.
Stdin has one command per line; blank lines are skipped:
- `F n`: n is digits only. Move forward one cell at a time n times. After each step the cell entered is drawn if the
  pen is down. If the next cell would be outside the grid, the turtle stops moving for the rest of this command.
- `R` / `L`: turn 90 degrees right / left (heading cycles N, E, S, W; north is toward row 0)
- `U` / `D`: pen up / pen down. `D` also draws the current cell.
Any other line (wrong word count, bad number, unknown command) is ignored but counted as bad.

Output: the 6 rows (12 characters each, `#` drawn, `.` not), then `pos=X,Y dir=H bad=K` where H is N, E, S or W.

Example: `F 3`, `R`, `F 2` prints
```
####........
...#........
...#........
............
............
............
pos=3,2 dir=S bad=0
```
Empty input draws only the start cell: a single `#` at the top left, `pos=0,0 dir=E bad=0`.
