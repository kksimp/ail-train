# group by

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query. If the input is empty, print nothing.

Queries (words separated by spaces):
- `count G` or `count G byvalue`: number of rows per distinct value of column G.
- `sum V G` or `sum V G byvalue`: sum of integer column V per distinct value of column G. A row whose V is not an
  integer (optional `-` and digits) is ignored completely (its group does not appear because of it) and counted as skipped.

For each query print `> ` plus the query with outer spaces trimmed, then one line `KEY VALUE` per group, then, only
when the skipped count is above 0, `(skipped N)`. Groups are ordered by key (byte order); with `byvalue` by value
descending, ties by key. Error lines replace everything after the `> ` line: `error: bad query` (unknown first word,
missing or leftover words), `error: unknown column X` (the group column is checked first, then the value column).

Example input:
    city,amt
    oslo,5
    rome,x
    oslo,7

    count city
    sum amt city
Output:
    > count city
    oslo 2
    rome 1
    > sum amt city
    oslo 12
    (skipped 1)
