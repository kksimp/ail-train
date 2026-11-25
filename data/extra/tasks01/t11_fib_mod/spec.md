# Fibonacci modulo queries

Answers queries for Fibonacci numbers modulo M, where F(0) = 0, F(1) = 1, F(k) = F(k-1) + F(k-2).

Input: each non-blank line is one query `N M`, exactly two integers (an optional `-` and digits, separated by whitespace) with 0 <= N <= 1000000000000000000 and 1 <= M <= 1000000000. For such a query print `N M R` where R = F(N) mod M (N and M printed as numbers, so leading zeros disappear). Any other non-blank line prints `error`. Blank lines are ignored.

N can be huge, so a program that adds up Fibonacci numbers one at a time will be too slow.

Example input:
```
10 1000
100 1000000007
0 1
7 abc
```
Output:
```
10 1000 55
100 1000000007 687995182
0 1 0
error
```

Edge cases: M = 1 always gives R = 0; empty input prints nothing.
