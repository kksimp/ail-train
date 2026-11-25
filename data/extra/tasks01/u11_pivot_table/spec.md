# pivot table

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Queries: `pivot R C count` or `pivot R C sum V` (R, C, V column names, exactly 4 or 5 words as shown). The result is a
grid whose rows are the distinct R values and whose columns are the distinct C values, both in byte order. A cell holds the
row count (`count`) or the sum of integer V values (`sum`) for rows with that R and C; a row whose V is not an integer
(optional `-` and digits) is ignored. A cell with no counted rows prints `.`.

Print `> ` plus the query, then the grid: a header line `R,c1,c2,...,total`, one line per row value
`r,cell1,cell2,...,rowtotal` (total = sum of that row's cells, `.` counted as 0), and a last line `total,` followed by the
column totals and the grand total, all comma-joined. When no row is counted, print only `(empty)` after the `> ` line.
Errors: `error: bad query` (wrong word count or keyword), `error: unknown column X` (checked in order R, C, V).

Example input:
    r,c,v
    a,x,1
    a,y,2
    b,x,5
    a,x,3

    pivot r c sum v
Output:
    > pivot r c sum v
    r,x,y,total
    a,4,2,6
    b,5,.,5
    total,9,2,11
