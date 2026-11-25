# distinct values per column

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Queries:
- `distinct *`: one line `NAME: N` per column in header order, N the number of distinct values in that column.
- `distinct COL`: one line `COL (N): v1, v2, ...` listing the distinct values in order of first appearance.
- `distinct COL sorted`: the same line with the values sorted. If every value in the column is an integer (optional `-`
  and digits) and the column has at least one row, sort numerically ascending; otherwise by bytes ascending.
An empty value is shown as `<empty>` in lists. A column with no rows prints `COL (0): -`.

Each query is echoed as `> ` plus the query. `error: bad query` is printed when the first word is not `distinct`, the
second word is missing, there are more than three words, or a third word is not `sorted` (or is given with `*`).
`error: unknown column X` is printed when COL is not in the header.

Example input:
    a,b
    x,1
    y,
    x,10

    distinct a
    distinct b sorted
    distinct *
Output:
    > distinct a
    a (2): x, y
    > distinct b sorted
    b (3): <empty>, 1, 10
    > distinct *
    a: 2
    b: 3
