# Garden grid

Simulate plants growing on a rectangular grid of garden cells that are watered by hand.

## Input (standard input)

- Line 1 (header): two whitespace-separated tokens `ROWS COLS`, each made of decimal digits only and between 1 and 8. If the input is empty or the header is invalid, print only `bad header` and stop. The header line is never treated as a comment.
- Every following line is a command. Words are separated by spaces; surrounding whitespace is ignored. Lines that are empty or start with `#` are skipped silently but count for line numbers (1-based, the header is line 1).

Commands:

- `plant R C`: put a new plant at row `R`, column `C` (1-based, row 1 is the top). `R` and `C` must consist of decimal digits only.
- `water R C`
- `day`
- `show`

## State

Every cell holds: whether it has a plant, the plant's height (1 to 9), an amount of water (an integer, initially 0) and a count of consecutive dry days for its plant. Water belongs to the cell, with or without a plant. Initially no cell has a plant.

## Rules

- `plant`: the cell gets a plant with height 1 and dry count 0 (the water already in the cell stays).
- `water R C`: add 3 water to that cell and 1 water to each of its existing orthogonal neighbours (up, down, left, right; cells outside the grid are ignored).
- `day`: first, visit every cell that has a plant, in row-major order (row 1 left to right, then row 2, ...), using that cell's own water only:
  - If its water is at least 2: subtract 2 from the water, set the dry count to 0, and if the height is below 9 add 1 to the height (this is growth; when the height reaches 9 it counts as one bloom).
  - Otherwise: add 1 to the dry count; if the dry count is now 3, the plant dies: the cell has no plant any more (height 0, dry count 0, its water is kept) and the death is counted.
  
  Second, after all plants were visited, every cell's water is halved (integer division, rounding down), planted or not.
  
  The day counter then increases (the first day is day 1). Print `day D: grew G died K` where G is the number of plants whose height increased on this day and K the number of plants that died on this day.
- `show`: print one line per grid row, one character per cell: the plant's height digit, or `.` for a cell with no plant.

## Errors

An invalid command prints `error line N: MESSAGE` (N is the input line number) and does nothing else. Checks, in this order, the first failing one is reported:

1. `unknown command`: the first word is not `plant`, `water`, `day` or `show`.
2. `bad arguments`: `day` or `show` with any extra word; `plant` or `water` without exactly two further words, or where a further word is not digits only (so `-1`, `x` and `+1` are not numbers).
3. `out of range`: `R` is not between 1 and ROWS, or `C` is not between 1 and COLS (checked for both `plant` and `water`).
4. `cell occupied`: `plant` on a cell that already has a plant.

## Output

All lines described above, in input order. After the last input line print one summary line:

```
summary: blooms B dead D alive A
```

with the total number of blooms, the total number of plants that died, and the number of plants alive at the end.

## Example

Input:

```
3 4
plant 1 1
plant 2 2
plant 3 4
show
water 1 2
water 2 2
day
show
water 2 2
water 3 3
day
water 3 4
day
show
day
day
show
```

Output:

```
1...
.1..
...1
day 1: grew 1 died 0
1...
.2..
...1
day 2: grew 1 died 0
day 3: grew 1 died 1
....
.3..
...2
day 4: grew 0 died 0
day 5: grew 0 died 1
....
....
...2
summary: blooms 0 dead 2 alive 1
```
