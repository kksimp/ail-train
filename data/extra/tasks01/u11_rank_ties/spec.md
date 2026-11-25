# rank with ties

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Query: `rank V MODE` or `rank V MODE asc`, where V is an integer column, MODE is `standard` or `dense`. Rows whose V is not
an integer (optional `-` and digits) are ignored. By default the largest value gets rank 1; with `asc` the smallest does.
Rows with equal V share a rank. `standard` ranking gives the next distinct value the rank equal to 1 plus the number of
rows ranked before it (1, 2, 2, 4); `dense` gives it the previous rank plus 1 (1, 2, 2, 3).

Print `> ` plus the query, then one line `RANK ID V` per ranked row, ordered by rank, ties in table order, where ID is the
row's first column. If no row is ranked print `(none)`. Errors: `error: bad query` (first word not `rank`, MODE not
`standard`/`dense`, a fourth word other than `asc`, wrong word count), `error: unknown column X` (for V).

Example input:
    id,score
    a,90
    b,85
    c,90
    d,70

    rank score standard
    rank score dense asc
Output:
    > rank score standard
    1 a 90
    1 c 90
    3 b 85
    4 d 70
    > rank score dense asc
    1 d 70
    2 b 85
    3 a 90
    3 c 90
