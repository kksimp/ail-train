# moving_avg

Reads a window size and a series of integers from standard input and prints the moving average of the series.

## Input

- Line 1: the window size K, a decimal integer (surrounding spaces are ignored).
- Every following line: zero or more values separated by spaces. Together, the values on all following lines form the series, in order. A value is a non-empty run of ASCII digits (a non-negative integer).

## Rules

1. If line 1 is missing, is not an integer, or is less than 1, print `bad window` and stop.
2. If any value of the series is not a run of digits (for example `-3`, `+4`, `2.5`, `x`), print `bad value` and stop.
3. If the series has fewer than K values, print `none` and stop.
4. Otherwise, for every position where K consecutive values end (the first window is values 1..K, the next is values 2..K+1, and so on), compute the sum of the K values in the window divided by K, rounded down to an integer.

Rules 1, 2 and 3 are checked in that order.

## Output

The averages, in window order, separated by single spaces, on one line.

## Example

Input:

```
3
4 8 6
10 1 7 7
```

Output:

```
6 8 5 6 5
```
