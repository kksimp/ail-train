# Column alignment of a table

The first input line is the alignment line: zero or more space-separated letters `l`, `r` or `c` (left, right,
center), one per column. Any other token makes the program print `bad spec` and nothing else. Every later line is a
table row whose cells are separated by `|`; each cell is trimmed of leading and trailing spaces/tabs. Rows with no
non-space characters are skipped. Empty input prints nothing.

The table has as many columns as the widest row; a shorter row has empty cells at its end. A column without a letter
in the alignment line is left-aligned. Each column is as wide as its longest cell. Pad every cell to its column width
(`l`: text then spaces; `r`: spaces then text; `c`: spaces on both sides, and when the padding is odd the extra space
goes on the right). Join the cells of a row with ` | ` (space, bar, space), remove trailing spaces from the end of the
line, and print the row.

Example input:

    l r c
    name | qty | ok
    pen|3|y
    notebook | 12 | no

Example output:

    name     | qty | ok
    pen      |   3 |  y
    notebook |  12 | no
