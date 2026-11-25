# 0/1 knapsack

Picks items to maximise total value without exceeding a weight capacity; each item can be taken at most once.

Input: the first non-blank line is the capacity C, a single non-negative integer (digits only). If it is missing, malformed, or larger than 10000, print `bad capacity` and nothing else. Every later non-blank line `W V` (exactly two integers, optional `-` and digits) with W at least 1 and V at least 0 is an item. Any other non-blank line is skipped and counted.

Output, exactly four lines:
- `items N` the number of valid items.
- `skipped K` the number of skipped lines.
- `best B` the maximum total value achievable with total weight at most C (0 if nothing fits).
- `weight W` the smallest total weight among selections that reach value B (0 when B is 0).

Example input:
```
10
5 10
4 40
6 30
3 50
```
Output:
```
items 4
skipped 0
best 90
weight 7
```

Edge cases: an item heavier than C is simply never taken; items of value 0 never raise the value.
