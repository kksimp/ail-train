# Pascal's triangle rows

Prints rows of Pascal's triangle. Row 0 is `1`; row K lists the binomial coefficients C(K,0) .. C(K,K).

Input: each non-blank line is one token. If the line (surrounding whitespace removed) is made of digits only and its value K is at most 60, print `K: ` followed by the K+1 entries of row K separated by single spaces, then ` | sum S` where S is the sum of the row. Any other non-blank line prints `TEXT invalid`, TEXT being the trimmed line. Blank lines are ignored.

Example input:
```
0
4
x
```
Output:
```
0: 1 | sum 1
4: 1 4 6 4 1 | sum 16
x invalid
```

Edge cases: empty input prints nothing. All values fit in 64-bit signed integers for K up to 60.
