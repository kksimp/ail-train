# rpn: an RPN calculator with variables

Reads lines from stdin; each line is a sequence of tokens separated by spaces, evaluated left to right on an
integer stack that starts empty at the beginning of every line. Variables persist from line to line (an assignment
stays even if the same line fails later). Blank lines (nothing but spaces) are skipped and print nothing.

Tokens:
- an integer, an optional `-` then digits (`7`, `-12`): push it
- `+ - * / %`: pop b, then a, push a OP b. `/` and `%` truncate toward zero (`-7 / 2` is -3, `-7 % 2` is -1)
- a name, 1 or more lowercase letters: push the variable's value
- `=name` (`=` followed by a name): pop a value and store it in the variable
- anything else is a bad token

Each non-blank line prints one line: the stack from bottom to top separated by single spaces, or `(empty)` if the
stack is empty. If something goes wrong, the line prints only the first error, and evaluation of that line stops:
- `error: stack underflow` (an operator or `=name` finds too few values)
- `error: division by zero` (`/` or `%` with b = 0)
- `error: unknown variable NAME` (a variable that was never assigned)
- `error: bad token TOKEN`

Example: the lines `3 4 + =x`, `x x *`, `x y` and `5 0 /` print
```
(empty)
49
error: unknown variable y
error: division by zero
```
Empty input prints nothing.
