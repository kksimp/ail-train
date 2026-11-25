# rain_water

For each height map on its own line, computes how much rain water it traps.

Input: each line is a height map, whitespace-separated non-negative integers (each a column's height, width 1). A blank line is an empty map. A trailing newline is not an extra line.
A line containing any token that is not a non-negative integer (digits only; valid tokens have at most 9 digits) prints `bad`.
Otherwise print the units of water held after rain: the water above a column is min(tallest column to its left or itself, tallest column to its right or itself) minus its own height; the total is the sum over all columns.

Output: one line per input line, in order: the total, or `bad`. An empty map holds 0.
After all lines print `max W` where W is the largest total among the valid lines, or `max none` if there were no valid lines (including empty input).

Example input:
```
0 1 0 2 1 0 1 3 2 1 2 1
3 0 3
```
Output:
```
6
3
max 6
```
