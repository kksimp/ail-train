# d5_resistor_net

Write a command-line program that reads descriptions of series/parallel resistor networks from standard input and prints the equivalent resistance of each, plus two structural measures.

## Input

Zero or more lines, numbered from 1. A line that is empty or contains only whitespace is ignored (but still counts in the numbering). Every other line holds one expression. No line is longer than 200 characters.

Grammar of an expression. The only whitespace that may appear is the space character; it is allowed between any two tokens and before or after the whole expression, but never inside a number.

```
expr   := number | 'S' '(' list ')' | 'P' '(' list ')'
list   := expr { ',' expr }
number := one or more ASCII digits
```

A number is a resistance in milliohms and must have a numeric value between 1 and 10000000 inclusive (leading zeros are allowed and do not matter; the value 0 and values above 10000000 are out of range, however many digits they have).

`S(...)` is a series connection and `P(...)` a parallel connection.

## Rules

- A number evaluates to itself.
- `S(a, b, c, ...)` evaluates to the sum of its items.
- `P(a, b, c, ...)` is evaluated by folding from the left: start with the first item, then combine the running value r with the next item x as `round(r * x / (r + x))`, where round is to the nearest whole milliohm with exact halves rounded up. Use integer arithmetic: `(2*r*x + r + x) / (2*(r + x))` with integer (floor) division. Every intermediate result is rounded this way, so the order of items matters.
- A list with a single item evaluates to that item (for both `S` and `P`).
- `depth` is 0 for a number, and for `S`/`P` it is 1 plus the largest depth among its items.
- `leaves` is the number of numbers in the whole expression.

All intermediate values fit in 64 bits.

## Errors

Parsing is left to right and stops at the first error found. Columns are 1-based positions in the original line (spaces count). The messages are:

- an expression is expected but the next non-space character is not a digit, `S` or `P` (or the line has ended): `expected value at column C`, C being the position of that character (the position just past the end of the line when it ended);
- a number is out of range: `out of range at column C`, C being the position of its first digit;
- `S` or `P` is not followed (after optional spaces) by `(`: `expected '(' at column C`, C being the position of the next non-space character (just past the end if none);
- inside a list, after an expression the next non-space character is neither `,` nor `)`: `expected ',' or ')' at column C` (position of that character, or just past the end);
- after a complete expression there is more non-space text: `trailing input at column C` (position of the first such character).

## Output

One line per non-blank input line, in input order:

- success: `line K: R ohm depth=D leaves=N` where R is the resistance in ohms written with exactly three decimals (whole part is milliohms divided by 1000 with no leading zeros, the fraction is the remainder padded to 3 digits), D the depth, N the leaves.
- failure: `line K: error: MESSAGE` with the message text as given above.

## Example

Input:

```
S(100, 200)
P(100,100)
P(1, 2, 3)

S(P(10, 10), 5, P(S(1, 2), 6))
470
P(1,)
S 100
P(10,20) 5
S(0)
```

Output:

```
line 1: 0.300 ohm depth=1 leaves=2
line 2: 0.050 ohm depth=1 leaves=2
line 3: 0.001 ohm depth=1 leaves=3
line 5: 0.012 ohm depth=3 leaves=6
line 6: 0.470 ohm depth=0 leaves=1
line 7: error: expected value at column 5
line 8: error: expected '(' at column 3
line 9: error: trailing input at column 10
line 10: error: out of range at column 3
```
