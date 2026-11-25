# Closest pair of points

Reads integer points and reports the pair with the smallest squared Euclidean distance.

Input: every non-blank line that consists of exactly two integers `X Y` (an optional `-` and digits, separated by whitespace) is a point, numbered 1, 2, 3, ... in input order. Any other non-blank line is skipped and counted. Blank lines are ignored.

Output, exactly three lines:
- `points P` where P is the number of points read.
- `skipped K` where K is the number of skipped lines.
- If P is less than 2: `closest none`. Otherwise `closest I J D`, where D is the smallest value of (xi-xj)^2 + (yi-yj)^2 over all pairs, and I < J are the point numbers of the pair reaching it; among tied pairs pick the one with the smallest I, then the smallest J. Duplicate points give D = 0.

Example input:
```
0 0
10 10
3 4
11 10
```
Output:
```
points 4
skipped 0
closest 2 4 1
```

Edge cases: empty input gives `points 0`, `skipped 0`, `closest none`.
