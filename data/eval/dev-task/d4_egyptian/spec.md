# Egyptian fraction expansion (greedy)

Write a program that reads fractions `a/b` from standard input, one per line, and expands each into a sum of distinct
unit fractions using the greedy method.

## Input

Zero or more lines. Whitespace at the start and end of a line is removed first, and lines that are empty after that are
skipped. A remaining line is a *valid fraction* if it has the form `A/B` where `A` and `B` are each one or more ASCII
digits (leading zeros allowed, no sign, no spaces), and `1 <= A < B <= 1000`. Anything else is invalid.

## Rules

Greedy expansion of a valid fraction `A/B`, working with the exact rational value `x = A/B` kept in lowest terms:

1. While `x > 0`:
   - If the denominator of `x` (in lowest terms) is greater than 1000000000, stop: the expansion is *too large*.
   - Let `d` be the smallest integer with `1/d <= x`, that is `d = ceil(denominator / numerator)`. Record `d`.
   - Replace `x` by `x - 1/d`, again in lowest terms.
2. The recorded values `d1, d2, ...` are the denominators of the expansion, in the order found.

A fraction that is not in lowest terms (such as `2/4`) is expanded like its lowest-terms value.

## Output

For each non-empty line print one line:

- valid and fully expanded: `A/B = 1/d1 + 1/d2 + ...` (terms in the order found, joined by ` + `), where `A` and `B` are
  the numeric values read (no leading zeros);
- valid but too large: `A/B: denominator too large`;
- invalid: `TEXT: invalid`, where `TEXT` is the line after whitespace removal.

Empty input prints nothing.

## Example

Input:

```
5/6
4/13
2/4
5/121
1/0
```

Output:

```
5/6 = 1/2 + 1/3
4/13 = 1/4 + 1/18 + 1/468
2/4 = 1/2
5/121: denominator too large
1/0: invalid
```
