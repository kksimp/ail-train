# atbash with checksum

Reads lines from standard input. For every non-empty line print `TEXT|COUNT|SUM`, where:
- TEXT is the line with the Atbash cipher applied: each ASCII letter is replaced by its mirror in the alphabet (A and Z swap, B and Y swap, and so on; `a` becomes `z`), keeping its case. Every other character is unchanged.
- COUNT is the number of ASCII letters in the line.
- SUM is the checksum: take the letters of TEXT (the already transformed ones) in order; the i-th letter (counting from 1) has the value p, its position in the alphabet (A or a is 1, Z or z is 26); SUM is the total of p times i over all letters, modulo 97.

Empty lines print nothing. A line with no letters prints its text unchanged followed by `|0|0`.

Example:
```
Hello, World!
```
prints
```
Svool, Dliow!|10|94
```
Empty input prints nothing.
