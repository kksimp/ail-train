# let: an arithmetic language with let-bindings

Each non-blank line of stdin (blank = only spaces, skipped) is one expression; print its value or an error on one line.
Tokens, separated by optional spaces: integers of 1 to 6 digits (no sign), names of one or more lowercase letters,
and the symbols `+ - * / % ( ) =`. The names `let` and `in` are keywords and cannot be variable names.

Grammar (`-` unary is the only prefix operator):
- expr: `let NAME = expr in expr`, or a sum
- sum: term, then any number of `+ term` or `- term` (left associative)
- term: unary, then any number of `* unary`, `/ unary` or `% unary` (left associative)
- unary: `- unary` or an atom
- atom: an integer, a variable, or `( expr )`

`let x = A in B` evaluates A, then B with x bound to that value; the binding is visible only inside B (B extends as
far right as possible) and hides any outer x. `/` and `%` truncate toward zero (`-7 / 2` is -3, `-7 % 2` is -1).

Output per line: the integer, or `error: MSG`. Errors are found while evaluating left to right and the first one wins:
`error: unbound NAME` (variable not bound), `error: division by zero`, `error: overflow` (after a `+`, `-` or `*`
the result's absolute value is above 1000000000000), or `error: syntax` (anything not matching the grammar, including
a character that is not a token, an integer with more than 6 digits, and tokens left over after a complete expression;
a bad character or long integer anywhere in the line makes the whole line a syntax error before any evaluation).

Example: `let x = 5 in x * x - 1` prints `24`; `1 / 0 + y` prints `error: division by zero`.
Empty input prints nothing.
