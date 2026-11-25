# magic_sum_combos

Finds all sets of K distinct digits from 1 to 9 that add up to a target N.

## Input
One query per line (blank lines ignored, lines trimmed): `K N`, two non-negative integers separated by a single space.

## Output
For each valid query print a header `K N: COUNT` and then one line per set, the digits in increasing order separated by single spaces. Sets are listed in lexicographic order of their digit lists (so `1 2 6` comes before `1 3 5`). A query with COUNT 0 prints only the header.
A line that is not exactly two non-negative integers prints `invalid: TEXT` (the trimmed line). K = 0 is valid: the only set is the empty set when N is 0 (printed as an empty line), otherwise there are none. K above 9 simply has no sets.

## Example
Input:
```
3 9
2 18
```
Output:
```
3 9: 3
1 2 6
1 3 5
2 3 4
2 18: 0
```
