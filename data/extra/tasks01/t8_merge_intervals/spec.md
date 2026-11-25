# Merge intervals

Each input line describes a closed integer interval as `START END` (two integers separated by whitespace, negative
numbers allowed). A line is invalid if it does not consist of exactly two integers or if START > END; print
`bad line N` (N = 1-based line number) for each invalid line, in input order, before any other output. Blank lines
are skipped silently.

Merge the valid intervals: two intervals are merged when they overlap or touch, that is when the next one (in order
of START) starts at or before the current merged END. Print the merged intervals in increasing order, one per line,
as `START-END` (a single dash between; negative numbers are printed as they are, e.g. `-5--2`).

Finally print `covered: C` where C is the total number of integers covered by the union, i.e. the sum of
`END - START + 1` over the merged intervals. With no valid intervals print only `covered: 0`.

Example input:
```
1 3
8 10
2 6
15 18
6 7
9 x
5 4
```
Output:
```
bad line 6
bad line 7
1-10
15-18
covered: 14
```
