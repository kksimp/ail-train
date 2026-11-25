# nqueens_count

Reads board sizes from standard input, one per line, and prints how many ways N queens can be placed on an N x N board so that no two attack each other (same row, column or diagonal).

## Input
One entry per line. Blank lines are ignored. Each entry is an integer N after trimming spaces.

## Output
For every entry print one line `N: COUNT`, in input order.
- If the entry is not an integer, or N is below 1 or above 9, print `invalid: TEXT` where TEXT is the trimmed line.
- Empty input prints nothing.

## Example
Input:
```
4
6
x
10
```
Output:
```
4: 2
6: 4
invalid: x
invalid: 10
```
