# join two tables

The input holds two tables and then queries, separated by lines that are exactly `--`. Each table is a header line
(comma-separated column names) followed by data rows with the same number of fields. The third section is queries, one per
line; blank lines in it are ignored. If any `--` is missing, print nothing.

A query is `inner KEY` or `left KEY`, where KEY is a column name present in both tables. The result has the columns of
the first table followed by the columns of the second table except KEY. For each first-table row in order, emit one result
row per second-table row (in table order) whose KEY value is equal as text. With `left`, a first-table row with no match
emits one row with the second table's columns left empty. `inner` drops unmatched rows.

Per query print `> ` plus the trimmed query, then the result header, the result rows (comma-joined), and `(N rows)`.
Errors replace everything after the `> ` line: `error: bad query` (not exactly two words, or first word not inner/left),
or `error: no column X` (KEY missing: the first table is checked, then the second).

Example input:
    id,name
    1,ann
    2,bob
    --
    id,pet
    1,cat
    1,dog
    --
    left id
Output:
    > left id
    id,name,pet
    1,ann,cat
    1,ann,dog
    2,bob,
    (3 rows)
