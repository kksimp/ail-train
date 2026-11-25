# truth: boolean expression truth tables

Each non-blank line of stdin is one boolean expression. Blank lines (only spaces) are skipped. Spaces are ignored.
Tokens: single lowercase letters (variables), `0`, `1`, `!` (not), `&` (and), `^` (xor), `|` (or), `(` and `)`.
Precedence from tightest: `!`, then `&`, then `^`, then `|`; the binary operators are left associative; `!` applies
to the item right after it (`!!a` is allowed, `!(a|b)` too). Any other character, or a malformed expression
(missing operand, unbalanced parentheses, two operands in a row, trailing tokens), is a syntax error.

For each expression print:
1. `expr: ` followed by the line with leading and trailing spaces removed
2. then, if the expression is a syntax error, the single line `syntax error`;
   if it uses more than 4 distinct variables, the single line `too many variables`;
   otherwise the table: with no variables, one line `f = V`. With variables, a header `a b | f` (the distinct
   variables in alphabetical order, separated by spaces, then ` | f`), then one row per assignment, bits in the
   same order and the result after `| `: e.g. `0 1 | 1`. Rows go from all 0 up to all 1 counting in binary, the first
   variable being the most significant bit.
   After the table, one line: `tautology` (always 1), `contradiction` (always 0) or `contingent`.

Example: the line `a & !b` prints
```
expr: a & !b
a b | f
0 0 | 0
0 1 | 0
1 0 | 1
1 1 | 0
contingent
```
Empty input prints nothing.
