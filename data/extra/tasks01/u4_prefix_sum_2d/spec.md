# 2D prefix sums with point updates

The first line holds R and C (1 <= R, C <= 20), the grid size. The next R lines each hold C integers separated by spaces. Every following line is a command; blank lines are ignored. Rows and columns are numbered from 0.

Commands and output (one output line per command):
- `sum R1 C1 R2 C2`: print the sum of the rectangle with corners (R1, C1) and (R2, C2), both inclusive; requires R1 <= R2 and C1 <= C2.
- `set R C V`: set cell (R, C) to V. Prints `ok`.
- `add R C V`: add V to cell (R, C). Prints `ok`.
- `total`: print the sum of the whole grid.
- `rowsums`: print, for each row, the sum of that row, separated by single spaces.

A `sum`, `set` or `add` whose coordinates are outside the grid, or a `sum` with R1 > R2 or C1 > C2, prints `out of range`. Any other line (unknown command, wrong number of words, non-integer argument) prints `error`. Neither changes the grid.
If the header or grid rows are malformed (wrong number of values, non-integers, missing lines), print `bad grid` and nothing else.

Example input:
    2 3
    1 2 3
    4 5 6
    sum 0 1 1 2
    set 1 1 0
    sum 0 0 1 1
    total
    rowsums
Output:
    16
    ok
    5
    16
    6 10
