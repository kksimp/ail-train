# int_stats

Reads integers and prints summary statistics.

Input: whitespace-separated tokens over any number of lines. A token that is an integer (optional leading `-`, 1 to 9 digits) is a value; any other token is counted as skipped.

Output, one line each, in this order (all on stdout):
```
count N
sum S
min A
max B
mean M
median D
mode V (xC)
skipped K
```
- `mean` is S/N printed with exactly 2 decimals, truncated toward zero (negative means keep the sign, but a mean that truncates to zero prints `0.00`).
- `median` is the middle value of the sorted values when N is odd; when N is even it is the average of the two middle values, printed as an integer if the sum of the two is even and with `.5` otherwise (for example 2 and 3 give `2.5`, -3 and -2 give `-2.5`, and 1 and 1 give `1`; the average is computed exactly, so -1 and 0 give `-0.5`).
- `mode` is the most frequent value and `C` its count; ties go to the smallest value.

If there are no values print only `no values` followed by the `skipped K` line.

Example input: `4 1 4 2 x 3`
```
count 5
sum 14
min 1
max 4
mean 2.80
median 3
mode 4 (x2)
skipped 1
```
