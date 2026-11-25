# CSV column totals

Standard input is a CSV-like table with no quoting: the first line is a header of column names separated by commas;
every following line is a data row of cells separated by commas. Lines are separated by `\n`; blank lines are ignored.

A data row whose number of cells differs from the header's is skipped (not counted anywhere).

For each column, in header order, print one line:

    name: TOTAL      if every cell of that column (over the kept rows) is an integer
    name: -          otherwise

An integer is an optional `-` followed by one or more digits (no spaces, no `+`). TOTAL is the sum of the column.
A column with no kept rows has TOTAL 0.

After the column lines, if at least one row was skipped, print `skipped: N` with the number of skipped rows.

If the input has no header line (empty or only blank lines), print `empty` and nothing else.

Example input:

    item,qty,price,note
    pen,3,-2,ok
    ink,x,10,fine
    pad,4,7
    cap,5,1,

Example output:

    item: -
    qty: -
    price: 9
    note: -
    skipped: 1
