# factorize

Reads one integer per line and prints its prime factorization.

Input: each line holds one token. Empty lines (after trimming whitespace) are skipped. A valid token is a decimal integer from 2 to 1000000000000 (10^12) with no sign and no other characters.

Output: for each non-empty line, one line `N = P1^E1 * P2^E2 ...` with primes ascending; an exponent of 1 is omitted (`12 = 2^2 * 3`), and a prime number prints as `N = N` followed by ` (prime)`, e.g. `13 = 13 (prime)`. A non-empty line that is not a valid token prints `line K: invalid` where K is its 1-based physical line number. A valid token below 2 (0 or 1) or above 10^12 also prints `line K: out of range`.

Rules for deciding between the two errors: if the token is all digits (at least one) and its value is 0 or 1 or above 10^12, print `out of range`; anything else that is not all digits prints `invalid`.

Last, print `factored C` where C is the number of lines that produced a factorization.

Example input:
```
12
13
abc
1
360
```
Output:
```
12 = 2^2 * 3
13 = 13 (prime)
line 3: invalid
line 4: out of range
360 = 2^3 * 3^2 * 5
factored 3
```
