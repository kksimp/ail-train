# cum_rank

Reads integer scores and prints, for every distinct score, its cumulative percent rank.

## Input

Zero or more lines, each holding scores separated by spaces. Together all the scores form the data. A score is an optional `-` followed by one or more ASCII digits (so `-5`, `0` and `42` are scores; `+5`, `1.5`, `-` and `x` are not).

## Rules

1. If any token is not a score, print `bad value: TOKEN` (the first such token in input order) and stop.
2. If there are no scores at all, print `no data` and stop.
3. Let N be the number of scores (repeats count). For each distinct score V, let COUNT be how many times V occurs and CUM be how many scores are less than or equal to V.
4. The percent rank of V is CUM * 100 / N, rounded to the nearest integer, with an exact half rounded up. (Computed in integers: (CUM * 200 + N) divided by (2 * N), integer division.)

## Output

First the line `n: N`, then one line per distinct score in ascending numeric order, with four fields separated by single tab characters:

```
V<TAB>COUNT<TAB>CUM<TAB>PCT%
```

where PCT is the percent rank followed by a `%` sign.

## Example

Input:

```
5 3 9 5
3 -2 5
```

Output (the four fields of each row are separated by single tab characters):

```
n: 7
-2	1	1	14%
3	2	3	43%
5	3	6	86%
9	1	7	100%
```
