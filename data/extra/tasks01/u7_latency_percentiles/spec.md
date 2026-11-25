# Latency percentiles per endpoint

Read lines `ENDPOINT MILLIS` from standard input: ENDPOINT is a non-empty word, MILLIS is digits only, separated by one
space. Other non-empty lines are malformed (skipped and counted); empty lines are ignored.

For every endpoint, in ascending byte order, and then for all samples together under the name `ALL`, print one line
`NAME COUNT P50 P90 P99 MAX` using the nearest-rank method: sort the n samples ascending; the p-th percentile is the
sample at 1-based rank ceil(p * n / 100). MAX is the largest sample. After these lines print `malformed: K`.
If there are no valid samples print only `malformed: K` (no `ALL` line).

Example input:
```
/a 10
/a 20
/a 30
/b 5
```
Output:
```
/a 3 20 30 30 30
/b 1 5 5 5 5
ALL 4 10 30 30 30
malformed: 0
```
For `/a`: n = 3, rank of P50 is ceil(1.5) = 2, so 20; P90 and P99 have rank 3.
