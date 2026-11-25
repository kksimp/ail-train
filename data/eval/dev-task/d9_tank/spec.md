# Water tank

Simulate a water tank that is filled and then drained in each step.

## Input (standard input)

- Blank lines (empty or only spaces) are ignored everywhere. Every other line is called a data line; all remaining rules count data lines only.
- The first data line has two integers separated by spaces: `CAPACITY LEVEL` (the tank size and the starting level; `0 <= LEVEL <= CAPACITY`).
- Every following data line is one step and has two non-negative integers separated by spaces: `IN OUT`. There may be extra spaces around the numbers. All lines are well formed.

## Rules

Keep a current level, a running overflow total and a running shortfall total (all start with level `LEVEL` and totals 0). For each step, in order:

1. Add `IN` to the level. If the level is now above `CAPACITY`, add the excess to the overflow total and set the level to `CAPACITY`.
2. Subtract `OUT` from the level. If the level is now below 0, add the missing amount (the negative of the level) to the shortfall total and set the level to 0.

## Output

For each step, number steps from 1, print one line:

```
step N: LEVEL
```

where `LEVEL` is the level after both parts of the step. After the last step print:

```
overflow X shortfall Y
```

If the first data line is the only data line, print just that final line (with 0 and 0). If there are no data lines at all, print only `no data`.

## Example

Input:

```
100 40
30 10
50 20
40 5
0 60
10 70
20 0
```

Output:

```
step 1: 60
step 2: 80
step 3: 95
step 4: 35
step 5: 0
step 6: 20
overflow 30 shortfall 25
```
