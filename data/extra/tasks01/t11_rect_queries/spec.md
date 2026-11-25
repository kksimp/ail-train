# Point in rectangle queries

Reads an axis-aligned rectangle and then a list of query points, and classifies each point.

Input: the first non-blank line is `X1 Y1 X2 Y2`, four integers (an optional `-` and digits, separated by whitespace); the two corners may be given in any order, so the rectangle spans min(X1,X2)..max(X1,X2) by min(Y1,Y2)..max(Y1,Y2). If there is no such first line (empty input, or the first non-blank line is not exactly four integers), print `no rectangle` and nothing else.

Every following non-blank line is a query. A query of exactly two integers `X Y` prints one word:
- `inside` if the point is strictly inside the rectangle,
- `boundary` if it is on the rectangle's edge (corners included),
- `outside` otherwise.
Any other query line prints `bad`.

After all queries print a summary line `inside A boundary B outside C bad D` with the counts.

Example input:
```
0 0 10 5
5 2
10 5
11 0
x y
```
Output:
```
inside
boundary
outside
bad
inside 1 boundary 1 outside 1 bad 1
```

A rectangle with zero width or height is valid: all of its points are then `boundary`.
