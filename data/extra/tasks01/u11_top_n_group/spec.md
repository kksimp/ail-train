# top N per group

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Query: `top N V by G`, exactly five words, the fourth being `by`. N is a positive integer, V the name
of an integer column, G the name of the grouping column. For each distinct G value in byte order print one line
`G: id=v, id=v, ...` listing up to N rows of that group with the largest V, largest first, ties in table order. `id` is
the first column of the row. Rows whose V is not an integer (optional `-` and digits) are ignored; a group left with no
rows is not printed. If no group is printed, print `(none)` instead.

Each query is echoed as `> ` plus the query. `error: bad query` when the shape is wrong or N is not a positive
integer; `error: unknown column X` for an unknown V (checked first) or G.

Example input:
    id,team,pts
    p1,red,5
    p2,red,9
    p3,blue,4
    p4,red,9

    top 2 pts by team
Output:
    > top 2 pts by team
    blue: p3=4
    red: p2=9, p4=9
