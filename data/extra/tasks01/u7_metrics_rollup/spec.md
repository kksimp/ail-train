# Metrics rollup per minute

Read metric samples from standard input, one per line: `TS NAME VALUE`. TS is digits only (seconds), NAME is a non-empty
word, VALUE is an integer with an optional leading `-` followed by digits. Fields are separated by single spaces.
Samples may come in any order. Other non-empty lines are malformed (skipped and counted); empty lines are ignored.

Group samples by minute (TS divided by 60, rounded down) and NAME. Print one line per group, ordered by minute and then
by NAME in ascending byte order:

`MINUTE_START NAME COUNT SUM MIN MAX`

where MINUTE_START is the first second of the minute (a multiple of 60). Finally print `malformed: K`.

Example input:
```
5 cpu 10
61 cpu 7
59 cpu 30
30 mem -4
```
Output:
```
0 cpu 2 40 10 30
0 mem 1 -4 -4 -4
60 cpu 1 7 7 7
malformed: 0
```
With no valid samples only `malformed: K` is printed.
