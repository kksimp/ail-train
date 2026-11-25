# running totals per key

The input is a table followed by queries. The first line is the header (comma-separated column names). Each line after
it up to the first blank line is a data row with the same number of fields. Every non-blank line after that blank line is
a query (outer spaces trimmed). If the input is empty, print nothing.

Queries, exactly four words: `running V by K` or `runmax V by K` (the third word must be `by`). Go through the rows in table
order, skipping rows whose V is not an integer (optional `-` and digits). For every other row print
`ID K: V -> R`, where ID is the row's first column, K its K value, and R is the running total of V over the rows with
the same K seen so far including this one (`running`), or the largest V among them (`runmax`). After the rows, print
`(skipped N)` only when N, the number of skipped rows, is above 0. If no row qualifies and none was skipped, print `(none)`.

Each query is echoed as `> ` plus the query. `error: bad query` for a wrong shape or first word,
`error: unknown column X` for an unknown V (checked first) or K.

Example input:
    id,acct,amt
    t1,a,10
    t2,b,5
    t3,a,-4
    t4,a,x

    running amt by acct
Output:
    > running amt by acct
    t1 a: 10 -> 10
    t2 b: 5 -> 5
    t3 a: -4 -> 6
    (skipped 1)
