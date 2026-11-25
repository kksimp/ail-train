# heat_map

Aggregates weighted points into a coarse grid of buckets.

Input: the first line is `W H B`: the area width, height and the bucket size (positive integers). Every following line is a point `X Y` or `X Y WEIGHT`: X and Y are integers (X is the column, Y the row, counted from 0), WEIGHT a positive integer (default 1). Blank lines are skipped. A line that does not have 2 or 3 integer fields (an optional `-` and digits), or whose weight is below 1, counts as bad. A point outside 0 <= X < W, 0 <= Y < H counts as ignored. If the first line is missing or is not three positive integers, print `error: bad header` and nothing else.

A valid point adds its weight to the bucket (Y / B, X / B) (integer division). The bucket grid has ceil(H / B) rows and ceil(W / B) columns.

Output: the bucket grid, one row per line, values separated by one space, each right-aligned to the width of the largest value. Then `total T ignored I bad M` (T is the sum of all added weights), then `hottest R,C V` with the first bucket in row-major order holding the largest value V, or `hottest none` if T is 0.

Example input:
```
5 3 2
0 0
1 1 4
4 2 3
9 9
x 1
```
Output:
```
5 0 0
0 0 3
total 8 ignored 1 bad 1
hottest 0,0 5
```
