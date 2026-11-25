# missing-value report

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

A value is missing when, after trimming spaces and ASCII lower-casing, it is empty or equals `na`, `n/a`, `null`,
`none` or `-`.

Queries (each echoed as `> ` plus the query):
- `missing`: one line `COL: N/T (P%)` per column in header order, N the missing values, T the number of rows,
  P = N * 100 / T rounded down (0 when T is 0).
- `missing rows`: one line `ID: c1,c2` per row (table order) with at least one missing value, ID the first column and
  c1,c2 the names of its missing columns in header order. If no row qualifies print `(complete)`.
- `missing COL`: one line `COL: id1, id2` with the first-column values of the rows where COL is missing, or `COL: -` if
  none. `rows` always means the second form.
`error: bad query` when the first word is not `missing` or there are more than two words;
`error: unknown column X` when COL is not in the header.

Example input:
    id,a,b
    r1,5,N/A
    r2, ,x
    r3,7,y

    missing
    missing rows
    missing b
Output:
    > missing
    id: 0/3 (0%)
    a: 1/3 (33%)
    b: 1/3 (33%)
    > missing rows
    r1: b
    r2: a
    > missing b
    b: r1
