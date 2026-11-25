# Magic square check

Reads a square grid of integers and says whether it is a magic square.

Input: the grid, one row per line, numbers separated by whitespace. Empty lines are skipped. A number is an optional `-` followed by digits.

Print exactly one line:
- `invalid` if there are no rows, any token is not a number, or the grid is not square (some row has a length different from the number of rows N).
- `not magic: numbers` if the grid is square but its N*N values are not exactly the numbers 1 to N*N, each once.
- Otherwise let S = N*(N*N+1)/2. Check the sums in this order and report the first that differs from S: each row top to bottom (`not magic: row R`, 1-based), each column left to right (`not magic: column C`), the main diagonal from top-left (`not magic: diagonal`), the other diagonal from top-right (`not magic: anti-diagonal`).
- If every sum equals S print `magic S` (with the number S).

Example input:
```
2 7 6
9 5 1
4 3 8
```
Example output:
```
magic 15
```

Empty input prints `invalid`.
