# Two-sum queries

The first input line is a list of integers separated by spaces (possibly empty, possibly with duplicates and
negative numbers). Every later non-blank line is a query holding one integer target T (optional `-` then digits,
surrounding spaces ignored).

For each query, find two different positions i < j (0-based) with `a[i] + a[j] == T`. If several pairs exist, choose
the one with the smallest j, and for that j the smallest i. Print `i j`. If there is no such pair, print `none`.
A query line that is not a single integer prints `bad query`.

Example input:
```
2 7 11 15 -3 7
9
18
4
100
x
```
Output:
```
0 1
2 5
none
none
bad query
```
(For target 18 the pairs are positions 2 and 5 (11 + 7); for target 4 there is none.)

Empty input prints nothing. If the first line is empty, every valid query prints `none`.
