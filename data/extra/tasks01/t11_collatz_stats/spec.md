# Collatz statistics

For each starting number, follows the Collatz rule (if n is even, n becomes n/2; if odd, n becomes 3n+1) until it reaches 1.

Input: each non-blank line is one token. If the line (surrounding whitespace removed) is made of digits only and its value is between 1 and 1000000, print `N steps S peak P` where N is the value (leading zeros dropped), S the number of rule applications needed to reach 1 (0 for N = 1) and P the largest value reached along the way (including N itself). Any other non-blank line prints `TEXT invalid`, TEXT being the trimmed line. Blank lines are ignored.

Finally print `longest N steps S` for the valid number with the most steps (the smallest such N on ties), or `longest none` if there was no valid number.

Example input:
```
6
1
27
abc
```
Output:
```
6 steps 8 peak 16
1 steps 0 peak 1
27 steps 111 peak 9232
abc invalid
longest 27 steps 111
```

Edge cases: empty input prints only `longest none`.
