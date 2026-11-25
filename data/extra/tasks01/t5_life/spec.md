Standard input: the first non-blank line is an integer S >= 0, the number of generations to simulate (at most 1000).
The remaining non-blank lines are a grid of `#` (live cell) and `.` (dead cell); any other character counts as dead.
Rows may have different lengths: pad shorter rows on the right with dead cells. The board is finite and everything outside it is dead.

Apply Conway's rules S times, all cells at once: a live cell with 2 or 3 live neighbours (of the 8 around it) stays alive,
a dead cell with exactly 3 live neighbours becomes alive, every other cell is dead.
Print the final grid, one row per line, using `#` and `.`, with all rows padded to the widest row.
If the first non-blank line is not a non-negative integer (including empty input) print `bad steps` and nothing else.
If there are no grid rows, print nothing.

Example input:
```
1
.#.
.#.
.#.
```
Output:
```
...
###
...
```
