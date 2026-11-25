# Convex hull vertex count

Reads integer points and reports how many corners their convex hull has.

Input: every non-blank line of exactly two integers `X Y` (an optional `-` and digits, separated by whitespace) is a point. Any other line is ignored. Duplicate points count once.

Output, exactly two lines:
- `distinct D` where D is the number of distinct points.
- `hull H` where H is the number of vertices of the convex hull, counting only true corners: points that lie on an edge between two corners (collinear points) are not vertices. For 0, 1 or 2 distinct points H equals D. If all points are collinear (3 or more distinct), H is 2 (the two extreme points).

Example input:
```
0 0
4 0
4 4
0 4
2 2
2 0
```
Output:
```
distinct 6
hull 4
```

Edge cases: empty input gives `distinct 0` and `hull 0`.
