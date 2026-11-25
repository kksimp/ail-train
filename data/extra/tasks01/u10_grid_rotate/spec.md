# grid_rotate

Reads a character grid followed by transform commands, and prints the transformed grid.

Input: the grid is the lines before the first empty line (all rows have the same width, no spaces needed; any non-empty characters). After the empty line come commands, one per line, trimmed of spaces; empty command lines are skipped.
Commands: `R` rotate 90 degrees clockwise, `L` rotate 90 degrees counter-clockwise, `H` mirror left-right, `V` flip top-bottom.

Output: the grid after applying all commands in order, one row per line. If a command is not one of the four, print the single line `error: bad command X` (X is the trimmed command) and nothing else. If the grid is empty (no rows before the empty line, or no empty line and no lines), print nothing.
If there is no empty line, the whole input is the grid and there are no commands.

Example input:
```
ab
cd
ef

R
```
Output:
```
eca
fdb
```
Note rotating clockwise turns the 3x2 grid into 2x3.
