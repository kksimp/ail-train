# Coin change: number of ways

Reads a set of coin values and then amounts, and for each amount counts the ways to make it. Orders do not matter (1+2 and 2+1 are the same way), and each coin value can be used any number of times.

Input: the first non-blank line lists coin values separated by whitespace. A token that is a positive integer (digits only) is a coin; any other token is ignored; repeated values count once. Every later non-blank line is a query.

A query that is a single non-negative integer A (digits only, at most 5000) prints `A WAYS`. A single non-negative integer above 5000 prints `A too large`. Any other query prints `TEXT invalid` where TEXT is the line with surrounding whitespace removed. A = 0 has exactly 1 way (use no coins); an amount that cannot be made has 0 ways.

Example input:
```
1 2 5
5
11
abc
-3
0
```
Output:
```
5 4
11 11
abc invalid
-3 invalid
0 1
```

Edge cases: empty input prints nothing. If the first line has no valid coins, only amount 0 has a way.
