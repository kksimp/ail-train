# line_of_sight

Marks which open cells of a map can be seen from the viewer.

Input: non-empty lines forming a grid of equal-width rows (empty lines ignored). `#` is a wall, `.` is open floor, `@` is the viewer. 
If the grid does not contain exactly one `@`, print `error: need exactly one @` and nothing else.

A cell is visible if every cell strictly between it and the viewer is not a wall. The cells between are found this way: let dr, dc be the row and column differences from the viewer to the target and n = max(|dr|, |dc|). For i = 1 .. n-1 the i-th cell is at row r0 + sign(dr) * q(|dr|*i) and column c0 + sign(dc) * q(|dc|*i), where q(x) = (2*x + n) / (2*n) with integer division (rounding to nearest, halves up). Walls themselves are never marked.

Output: the grid with every visible `.` replaced by `*` (other cells unchanged), then the line `visible K` with the number of `*`.

Example input:
```
.....
.#...
@.#..
```
Output:
```
*....
*#.**
@*#..
visible 5
```
