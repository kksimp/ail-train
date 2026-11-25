# ca1d: a one-dimensional cellular automaton

Line 1 of stdin is `RULE STEPS`: two integers (digits only) separated by one space, RULE from 0 to 255 and STEPS from
0 to 30. Line 2 is the start row: 1 to 40 characters, each `0` or `1`. Anything else (missing lines, wrong word
count, a value out of range, other characters in the row) prints only `bad input`.

The row wraps around: the left neighbour of the first cell is the last cell and the right neighbour of the last
cell is the first (in a row of 1 cell, a cell is its own left and right neighbour). In each step every cell gets a new
value at the same time: with l, c, r the left, own and right values, let i = 4*l + 2*c + r; the new value is bit i
(counting from bit 0 as the lowest) of RULE.

Print the start row and then the row after each step, STEPS + 1 lines in all, writing 1 as `#` and 0 as `.`.

Example: `90 2` with the row `00100` prints
```
..#..
.#.#.
#...#
```
Empty input prints `bad input`.
