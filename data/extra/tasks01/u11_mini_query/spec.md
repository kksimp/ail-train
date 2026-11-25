# mini query

The input is a table followed by queries. The first line is the header: comma-separated column names. Each following
line up to the first blank line is a data row with the same number of comma-separated fields. Every line after that
blank line that is not blank is a query. If the input is empty, print nothing.

A query is `select COLS`, then optionally `where COL OP VALUE`, then optionally `order COL` or `order COL desc`, in that
fixed order, words separated by spaces. COLS is `*` (all columns in header order) or comma-separated column names.
OP is one of `=`, `!=`, `<`, `>`, `<=`, `>=`. A column is numeric when it has at least one row and every value in it is an
integer (optional `-` and digits); otherwise it is text. Numeric columns compare as integers, text columns as strings
byte by byte. Ordering is stable: rows with equal keys keep table order; `desc` reverses the key order only.

For each query print `> ` and the query with outer spaces trimmed, then either the matching rows (selected columns joined
by commas, one row per line) followed by `(N rows)`, or a single error line instead of rows and count:
- `error: bad query`: wrong keyword order, missing words, unknown operator, or leftover words.
- `error: unknown column X`: first unknown name, checking the select list, then the where column, then the order column.
- `error: bad value V`: the where column is numeric but V is not an integer.

Example input:
    name,dept,age
    ann,eng,31
    bob,ops,27
    cy,eng,45

    select name,age where dept = eng order age desc
Output:
    > select name,age where dept = eng order age desc
    cy,45
    ann,31
    (2 rows)
