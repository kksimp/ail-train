Free slots in a calendar

The program reads a day's calendar from standard input and prints the free gaps.

Line 1 is the header: `open close minlen`, three integers (slot numbers) with open < close and minlen >= 1.
If the header is missing or malformed, print `bad header` and stop.

Every following non-blank line is a busy interval `start end` (two integers, start < end). Intervals may overlap,
touch, arrive in any order, and extend outside the day. A line that is not two integers with start < end is malformed:
it is counted and otherwise ignored.

Output: every free gap inside [open, close), in increasing order, one per line as `start-end`, but only gaps whose
length (end - start) is at least minlen. Busy time outside the day is ignored; touching or overlapping busy intervals
merge into one. Then print `free total T` (T is the sum of the printed gap lengths), then `skipped K`
(K is the number of malformed busy lines).

Example input:
```
9 17 2
10 12
11 13
15 16
13 14
oops
```
Busy time merges to 10-14 and 15-16, so the gaps are 9-10, 14-15 and 16-17, all of length 1. With minlen 2 none qualify:
```
free total 0
skipped 1
```
With header `9 17 1` the same lines print:
```
9-10
14-15
16-17
free total 3
skipped 1
```
A day with no busy lines prints the whole day as one gap if it is at least minlen long.
