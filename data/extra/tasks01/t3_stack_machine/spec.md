# stack machine

Read commands from standard input, one per line, and run them on an integer stack that starts empty.

Commands (words separated by spaces; blank lines are ignored but still count for line numbers):
- `push N`: push the integer N (optional leading `-`).
- `pop`: discard the top value.
- `dup`: push a copy of the top value.
- `swap`: exchange the top two values.
- `add`, `sub`, `mul`: pop b, then a, push `a+b`, `a-b`, `a*b`.
- `div`: pop b, then a, push a/b rounded toward zero. Division by zero is an error and leaves the stack unchanged.
- `print`: print the top value on its own line without removing it.

A failing line prints `line K: ERR` and changes nothing (K is the 1-based line number). ERR is `underflow` when the stack has too few values, `division by zero`, `bad number` for a missing or non-integer push argument, or `unknown command` for anything else (including extra words).

After all input, print `stack: ` followed by the values from bottom to top separated by single spaces (`stack:` alone if empty).

Example:
```
push 6
push 3
div
print
mul
```
prints
```
2
line 5: underflow
stack: 2
```
