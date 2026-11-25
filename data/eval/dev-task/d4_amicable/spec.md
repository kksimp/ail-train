# Amicable pairs up to N

Write a program that reads limits `N` from standard input, one per line, and for each prints the amicable pairs whose
larger member does not exceed `N`.

## Input

Zero or more lines. Whitespace at the start and end of a line is removed first, and lines that are empty after that are
skipped. A remaining line is a *valid limit* if it is an optional `-` followed by one or more ASCII digits (leading
zeros allowed) and its value is between 1 and 50000 inclusive. Anything else (a `+` sign, letters, a decimal point,
a value below 1 or above 50000) is invalid.

## Rules

Let `s(n)` be the sum of the proper divisors of `n` (all positive divisors of `n` except `n` itself; `s(1) = 0`).
An *amicable pair* is two integers `a < b` with `s(a) = b` and `s(b) = a`. (Perfect numbers, where `s(a) = a`, are
not pairs.) For a valid limit `N`, the pairs to report are those with `b <= N`, listed in increasing order of `a`.

## Output

For each valid limit print the line `N=VALUE: COUNT` where `VALUE` is the numeric value of the limit (no leading zeros)
and `COUNT` the number of pairs, followed by one line per pair: two spaces, `a`, a space, `b`.

For an invalid line print `TEXT: invalid`, where `TEXT` is the line after whitespace removal.

Empty input prints nothing.

## Example

Input:

```
300
1500
0
```

Output:

```
N=300: 1
  220 284
N=1500: 2
  220 284
  1184 1210
0: invalid
```
