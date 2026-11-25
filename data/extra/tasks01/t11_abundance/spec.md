# Perfect, abundant or deficient

Classifies positive integers by the sum S of their proper divisors (the divisors smaller than the number itself; 1 has none, so S(1) = 0).

Input: each non-blank line is one token. If the line (surrounding whitespace removed) is made of digits only and its value is between 1 and 1000000, print `N KIND S` where N is the value (leading zeros dropped), S the proper-divisor sum, and KIND is `perfect` if S equals N, `abundant` if S is greater than N, `deficient` if it is smaller. Any other non-blank line prints `TEXT invalid`, TEXT being the trimmed line. Blank lines are ignored.

After all lines print a summary: `perfect P abundant A deficient D invalid I`.

Example input:
```
6
12
7
28
0
x
```
Output:
```
6 perfect 6
12 abundant 16
7 deficient 1
28 perfect 28
0 invalid
x invalid
perfect 2 abundant 1 deficient 1 invalid 2
```

Edge cases: empty input prints only the summary with all zeros.
