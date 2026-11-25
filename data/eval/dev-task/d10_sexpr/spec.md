# S-expression calculator

Read lines from standard input; each non-blank line is one expression in a small Lisp-like notation over integers. Evaluate each and print the result or an error.

## Input
Lines are numbered from 1. A line that is empty or contains only whitespace (spaces/tabs) is skipped (it still counts for numbering and produces no output).

### Tokens
A line is split into tokens: the characters `(` and `)` are each a token by themselves; whitespace (space or tab) separates tokens and is otherwise ignored; any other maximal run of characters (containing no parenthesis and no whitespace) is one token (so `1.5`, `x`, `1-2` are each a single token).

### Grammar
```
expr := INT | "(" OP expr* ")"
```
- `INT` is a token consisting of an optional `-` followed by one or more digits `0-9` (leading zeros allowed, `-0` is 0; no `+` sign).
- `OP` is a token that is exactly one of `+`, `-`, `*`, `/`, `min`, `max` (case-sensitive), and must come immediately after `(`.
- A line must be exactly one `expr` with no tokens left over. Anything else is a **syntax error**: an empty expression `()`, a missing or invalid operator, an unknown token, unbalanced parentheses, a missing expression, or extra tokens after the expression.

## Evaluation
The whole line is checked for syntax errors first; if there is one, nothing is evaluated. Otherwise evaluate depth first: for a list, evaluate its arguments from left to right (the first error found ends the evaluation of the line), then check the number of arguments, then apply the operator:
- `+`: sum of the arguments; `*`: product; `min`/`max`: smallest/largest argument. These need at least 1 argument.
- `-`: with one argument, its negation; with two or more, the first minus the sum of the rest.
- `/`: exactly two arguments; integer division truncating toward zero (`-7 / 2` is `-3`). A zero divisor is a **division by zero** error.
- Wrong argument count (zero arguments for any operator, or not two for `/`) is a **bad arity** error. The arity check happens after the arguments were evaluated (so an error inside an argument is reported before an arity error of the enclosing list), and division by zero is checked after the arity check of that same list.
All results fit in 64-bit signed integers.

## Output
For each non-blank line print `N: RESULT` (N the line number, RESULT a decimal integer) or `N: error: MESSAGE` where MESSAGE is one of `syntax error`, `bad arity`, `division by zero`.

## Example
Input:
```
(+ 1 2 3)
(* 2 (- 10 4) 5)
(- 7)
(- 20 5 3)
42
(max 3 (min 8 -2 5) 1)
(/ (+ 100 5) 10)
(/ -7 2)
```
Output:
```
1: 6
2: 60
3: -7
4: 12
5: 42
6: 3
7: 10
8: -3
```
