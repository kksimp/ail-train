# Perfect power detection

Write a program that reads integers from standard input, one per line, and for each one reports whether it is a perfect
power, that is, whether it can be written as `b^e` with integers `b >= 2` and `e >= 2`.

## Input

Zero or more lines. Whitespace at the start and end of a line is removed first, and lines that are empty after that are
skipped. A remaining line is a *valid number* if it consists of an optional `-` followed by one or more ASCII digits
(leading zeros allowed) and its value is between 2 and 1000000000000 inclusive. Anything else (a `+` sign, letters, a
decimal point, inner spaces, a value below 2 or above 10^12) is invalid.

## Rules

For a valid number `n`, among all ways to write `n = b^e` with `b >= 2`, `e >= 2`, choose the one with the largest
exponent `e` (equivalently the smallest base `b`). For example 64 is `2^6`, not `8^2` or `4^3`.

## Output

For each non-empty line print one line:

- a valid number that is a perfect power: `N = B^E`, with `N` the numeric value (no leading zeros);
- a valid number that is not a perfect power: `N is not a perfect power`;
- an invalid line: `TEXT: invalid`, where `TEXT` is the line after whitespace removal.

Empty input prints nothing.

## Example

Input:

```
8
12
81
1
```

Output:

```
8 = 2^3
12 is not a perfect power
81 = 3^4
1: invalid
```
