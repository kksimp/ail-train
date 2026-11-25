# falling_sand

Simulates sand grains falling in a grid for a number of steps.

Input: the first line is the number of steps N (a non-negative integer). The following non-empty lines are the grid, rows of equal width: `.` empty, `#` rock (never moves), `o` sand. If the first line is not a valid non-negative integer print `error: bad steps` and nothing else.

One step handles rows from the second-to-last row up to the top row, and within a row columns from left to right. Each sand grain, when handled, moves to the first of these that is empty: straight down; down and to the left; down and to the right (it never moves if the row is the last). A grain moved in this step is not moved again in the same step, because the row it landed in has already been handled.

Output: the grid after N steps, one row per line, then `sand S` with the number of grains (unchanged by the steps).

Example input:
```
2
.o.
.o.
...
```
Output:
```
...
...
oo.
sand 2
```
