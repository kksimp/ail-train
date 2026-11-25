# Polygon doubled area

Reads a polygon from standard input and prints twice its area (so the answer is always an integer) and its orientation.

Input: the first non-blank line is the vertex count N. If it is not an integer, or is negative, N is 0. Each following non-blank line that consists of exactly two integers `X Y` (an optional `-` and digits, separated by whitespace) is a vertex, in order. Any other line is ignored. Only the first N vertices are used; fewer are used if the input has fewer. Blank lines are ignored everywhere.

Output, exactly two lines:
- `doubled_area A` where A is the absolute value of the shoelace sum over the vertices taken in order, closing from the last back to the first.
- `orientation O` where O is `ccw` if the signed shoelace sum is positive, `cw` if negative, and `degenerate` if it is 0 (including fewer than 3 vertices).

Example input:
```
4
0 0
4 0
4 3
0 3
```
Output:
```
doubled_area 24
orientation ccw
```

Edge cases: empty input prints `doubled_area 0` and `orientation degenerate`. A header of `3` followed by 5 vertices uses only the first 3.
