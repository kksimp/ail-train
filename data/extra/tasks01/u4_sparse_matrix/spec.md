# Sparse matrix updates and row sums

Read commands from standard input, one per line, and maintain a matrix of integers that is conceptually all zeros. Rows and columns are integers 0 to 999999.
Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `set R C V`: set cell (R, C) to V. Prints `ok`.
- `add R C V`: add V to cell (R, C). Prints `ok`.
- `get R C`: print the value of the cell (0 if never set).
- `rowsum R`: print the sum of all cells in row R.
- `colsum C`: print the sum of all cells in column C.
- `nnz`: print the number of cells whose value is not zero.
- `rows`: print the row numbers that contain at least one non-zero cell, ascending, separated by single spaces, or `none`.

V is any integer (possibly negative); a cell that becomes 0 counts as empty again. R or C outside 0..999999, a non-integer argument, an unknown command, or the wrong number of words prints `error` and changes nothing.

Example input:
    set 2 3 5
    add 2 3 -2
    set 2 7 4
    rowsum 2
    get 2 3
    nnz
    set 2 7 0
    nnz
Output:
    ok
    ok
    ok
    7
    3
    2
    ok
    1
