Standard input: the first non-blank line is an integer N >= 1, the side of a square chessboard (rows and columns numbered 0 to N-1).
Every following non-blank line is a query `r1 c1 r2 c2` (four integers separated by whitespace).

For each query print on its own line the minimum number of knight moves from (r1, c1) to (r2, c2) on the N by N board,
or `-1` if the target cannot be reached. A knight moves two squares in one direction and one square at right angles.
If a query line is not four integers, or any coordinate is outside the board, print `bad` for that query.
If the first non-blank line is not an integer >= 1 (including empty input), print `bad board` and nothing else.

Example input:
```
8
0 0 7 7
0 0 0 0
0 0 1 1
3 3 9 9
```
Output:
```
6
0
4
bad
```
