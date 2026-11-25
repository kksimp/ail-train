# Battleship shot log

Read a set of occupied cells and a series of shots on a 10 by 10 board, and report the result of each shot.

## Input

- Line 1: the occupied cells, separated by whitespace. A cell is a capital letter `A` to `J` (column) followed by a number `1` to `10` (row), for example `B7` or `J10`. This line is always valid, has at least one cell, and its cells are all different.
- Every following line is one shot: a single cell. Lines that are empty after trimming are skipped.

## Rules

- A shot is invalid if, after trimming, it is not a letter `A` to `J` followed by the decimal number `1` to `10` with no leading zeros and nothing else.
- A valid shot at a cell that was already shot earlier (valid shots only) is a `repeat`, whether or not it hit.
- Otherwise it is a `hit` if the cell is one of the occupied cells, and a `miss` if not.
- After a shot, if it was a `hit` and it was the last occupied cell to be hit, the result is `hit, fleet sunk` instead of `hit`. Shots after that continue to be reported normally (a shot at a new occupied cell cannot happen since all are hit).

## Output

One line per non-skipped shot, in input order: the trimmed shot text, a colon and a space, then the result: `hit`, `hit, fleet sunk`, `miss`, `repeat` or `invalid`.

## Example

Input:

```
A1 A2 C3
A1
B1
A1
K1
A02
A2
C3
C3
```

Output:

```
A1: hit
B1: miss
A1: repeat
K1: invalid
A02: invalid
A2: hit
C3: hit, fleet sunk
C3: repeat
```
