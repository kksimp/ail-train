# Spiral matrix print

Standard input is a matrix: each non-blank line is one row of integers separated by spaces (negative numbers
allowed). Blank lines are ignored.

Print the elements in clockwise spiral order, starting at the top-left corner, going right along the top row, then
down the right column, then left along the bottom row, then up the left column, and then inwards again, all on one
line separated by single spaces.

Special cases, each printing exactly one line:
- no rows at all: `empty`
- some token is not an integer: `invalid`
- rows have different numbers of elements: `ragged`
(`invalid` takes priority over `ragged`.)

Example input:
```
1 2 3 4
5 6 7 8
9 10 11 12
```
Output:
```
1 2 3 4 8 12 11 10 9 5 6 7
```
A single row prints left to right and a single column prints top to bottom.
