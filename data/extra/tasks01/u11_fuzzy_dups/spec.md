# fuzzy duplicate records

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Query: `dups SPEC`, exactly two words. SPEC is a comma-separated list of key columns, each `COL` or `COL:digits`.
A row's key is the list of its key columns' normalized values. `COL` uses the text rule: ASCII letters become lower
case, every character that is not an ASCII letter, digit or space is dropped, then runs of spaces collapse to one space
and outer spaces are removed. `COL:digits` keeps only the characters 0-9. A row whose key has any empty part is ignored.
Rows with equal keys are duplicates of each other.

Print `> ` plus the query, then for each key shared by 2 or more rows, in order of the first row of that key, a line
`group N: id1, id2, ...` (N counts from 1, ids are the rows' first column in table order), then
`(G groups, R records)` with G the number of groups and R the number of rows in them. If there are no groups print
`(no duplicates)` instead of the summary.
Errors: `error: bad query` (not two words, first word not `dups`, an empty item, or a suffix other than `digits`),
`error: unknown column X` (first unknown column, left to right).

Example input:
    id,name,phone
    1,J. Smith,555-0101
    2,j smith,(555) 0101
    3,Ann Lee,555-0199

    dups name,phone:digits
Output:
    > dups name,phone:digits
    group 1: 1, 2
    (1 groups, 2 records)
