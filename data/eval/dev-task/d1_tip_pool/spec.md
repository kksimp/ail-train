# tip_pool

Write `tip_pool`, a command-line program. It reads a restaurant's tip pool and the hours worked by each staff member from standard input, and prints each person's share of the pool.

## Input

- Blank lines (empty or only spaces) are ignored everywhere.
- The first non-blank line holds the pool `TOTAL`, a non-negative whole number of cents (for example `10000` is 100.00). If there is no such line, the pool is 0. You may assume the first line is a valid non-negative integer when it exists.
- Every later non-blank line should be `NAME HOURS`: exactly two fields separated by one or more spaces, `NAME` any text without spaces, `HOURS` a whole number of hours of 0 or more written with digits. A later line that does not fit this is ignored completely (it gets no output line). The same name may appear on several lines; each line is a separate person entry.

## Rules

Let `H` be the sum of the hours of all valid entries.

1. Each entry first gets `floor(TOTAL * hours / H)` cents.
2. The cents still undistributed (`TOTAL` minus the sum of those shares; always fewer than the number of entries with hours above 0) are handed out one cent each, going through the entries in input order and skipping entries with 0 hours, until none are left.

## Output

If `H` is 0 (this includes having no valid entries), print `no hours` and nothing else. Otherwise print one line per valid entry, in input order: `NAME: SHARE` where `SHARE` is the final amount in cents as a whole number.

## Example

Input:

```
10000
ana 8
ben 5
cy 0
bad line here
dee 6
```

Output:

```
ana: 4211
ben: 2632
cy: 0
dee: 3157
```

(Here `H` is 19. The floor shares are 4210, 2631 and 3157, which leaves 2 cents: one goes to `ana` and one to `ben`.)
