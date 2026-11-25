# Expression evaluator

Read standard input: one arithmetic expression per line. Blank lines (empty or only spaces) are skipped.

An expression uses non-negative integer literals, the binary operators `+ - * /`, unary minus, parentheses and spaces
anywhere between tokens. `*` and `/` bind tighter than `+` and `-`; operators of equal precedence group left to right;
unary minus binds tighter than any binary operator. `/` is integer division truncating toward zero.

For each non-blank line print one line:
- the integer value of the expression, or
- `error` if the line is not a valid expression (bad character, missing operand, unbalanced parenthesis, trailing junk,
  two numbers in a row), or
- `div0` if the (valid) expression divides by zero.
A syntax problem is reported even if a division by zero occurs earlier in the line.

Example input:
    1 + 2 * 3
    (1 + 2) * 3
    -7 / 2
    10 / (5 - 5)
    2 +

Example output:
    7
    9
    -3
    div0
    error

Empty input prints nothing.
