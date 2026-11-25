# theatre_seats

Seats groups of people in a theatre map.

Input: the map is the lines before the first empty line: rows of equal width, `.` is a free seat, `X` a taken seat, `_` an aisle (not a seat). The lines after the empty line are group sizes, one per line (blank lines skipped). A group size line that is not a positive integer (digits only, at least 1) prints `group K: invalid` (K is the 1-based number of the group request, invalid ones count) and seats nobody.

A group of size S needs S free seats side by side in one row (an aisle or a taken seat breaks the run). It is placed in the first row (from the top) that has such a run, at the leftmost such run. Its seats become `o`. If no row has a run, print `group K: none`. Otherwise print `group K: row R seats A-B` with R the 0-based row and A..B the 0-based columns (A equals B for a single seat).

Output: one line per group request in order, then the final map, then `free F` with the number of `.` seats left. If the map is empty, every valid group gets `none`, and the map prints no rows.

Example input:
```
.X..
....

2
3
```
Output:
```
group 1: row 0 seats 2-3
group 2: row 1 seats 0-2
.Xoo
ooo.
free 2
```
