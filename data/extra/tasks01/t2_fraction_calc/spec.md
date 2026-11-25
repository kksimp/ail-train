# fraction_calc

Evaluates exact fraction expressions, one per line, strictly from left to right (no operator precedence).

Input: each line is `OPERAND (OP OPERAND)*` with tokens separated by single or multiple spaces. An OPERAND is `N` or `N/D` where N and D are non-negative decimal integers of 1 or 2 digits (0 to 99), optionally with a leading `-` on N. OP is one of `+ - * /` (the symbol `/` as an operator is always a separate token, so `1/2 / 3/4` means (1/2) divided by (3/4)). An expression has at most 4 operands. Empty lines are skipped silently.

Output: for each expression, the exact result as a reduced fraction `N/D` with positive D, or just `N` if the denominator is 1. Zero prints `0`.

Errors (printed in place of the result; K is the 1-based physical line number):
- `line K: zero denominator` if an operand has D=0 or a division by zero occurs.
- `line K: bad expression` for anything else wrong (unknown token, operator in the wrong place, too many operands, a trailing operator).
When both apply, the one found first scanning tokens left to right while parsing is reported: the whole line is parsed before anything is evaluated, so a parsing problem (including an operand with D=0) is found before any division by zero during evaluation.

Finally print `evaluated N` with the number of results printed.

Example input:
```
1/2 + 1/3
3 / 4 * 2
5/0 + 1
7 +
-1/2 - -1/2
```
Output:
```
5/6
3/2
line 3: zero denominator
line 4: bad expression
0
evaluated 3
```
