# Continued fraction of a/b

Write a program that reads fractions `A/B` from standard input, one per line, and prints the simple continued fraction
expansion of each, followed by its convergents.

## Input

Zero or more lines. Whitespace at the start and end of a line is removed first, and lines that are empty after that are
skipped. A remaining line is *well formed* if it contains exactly one `/`, and each of the two parts is an optional `-`
followed by one or more ASCII digits (no `+`, no spaces, leading zeros allowed) whose absolute value is at most
1000000000. Anything else is invalid. A well-formed line whose denominator is 0 is a zero denominator.

## Rules

For a well-formed line with `B != 0`, let `(a, b) = (A, B)` if `B > 0`, and `(-A, -B)` if `B < 0`, so `b > 0`.

Expansion terms (Euclid's algorithm with floor division):

1. While `b != 0`: let `q = floor(a / b)` (rounding toward negative infinity, so `q` may be negative only for the first
   term) and `r = a - q*b` (so `0 <= r < b`); record `q`; then set `(a, b) = (b, r)`.
2. The recorded values `q0, q1, ..., qn` are the terms. The last term is not rewritten (no `... , k-1, 1` form).

Convergents: the k-th convergent is the value of `[q0; q1, ..., qk]` as a fraction `h_k/k_k` computed by
`h_k = q_k*h_(k-1) + h_(k-2)`, `k_k = q_k*k_(k-1) + k_(k-2)`, with `h_(-1) = 1, h_(-2) = 0, k_(-1) = 0, k_(-2) = 1`.
They are printed exactly as computed (the numerator may be negative, the denominator is positive).

## Output

For each non-empty line:

- invalid: print `TEXT: invalid`, where `TEXT` is the line after whitespace removal;
- zero denominator: print `TEXT: zero denominator`;
- otherwise print two lines:
  1. `A/B = SHAPE` where `A` and `B` are the numeric values as read (original signs, no leading zeros). `SHAPE` is
     `[q0]` if there is a single term, else `[q0; q1, q2, ..., qn]` (`; ` after the first term, `, ` between others).
  2. Two spaces, `convergents:`, then a space and the convergents `h/k` separated by single spaces, one per term.

Empty input prints nothing.

## Example

Input:

```
649/200
5/1
-7/2
1/0
x
```

Output:

```
649/200 = [3; 4, 12, 4]
  convergents: 3/1 13/4 159/49 649/200
5/1 = [5]
  convergents: 5/1
-7/2 = [-4; 2]
  convergents: -4/1 -7/2
1/0: zero denominator
x: invalid
```
