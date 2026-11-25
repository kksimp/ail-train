# csv_table

Read a simple CSV from standard input and print it as an aligned text table.

Input: lines of fields separated by `,`. There is no quoting; every comma separates fields. Blank lines (empty) are ignored. The first non-blank line is the header. Rows may have different numbers of fields: the table has as many columns as the longest row, and a short row is padded with empty cells.

Output:
- Column width is the largest cell length (in characters) in that column, header included.
- Each cell is padded on the right with spaces to its column width. Cells are joined with ` | `. Trailing spaces at the end of each output line are removed.
- After the header line comes a rule line: for each column, `-` repeated to the column width, joined with `-+-`.
- Then the remaining rows in input order.
- If there are no non-blank lines, print nothing.

Example input:
```
name,qty,note
apple,3
kiwi,12,green,extra
```
Example output:
```
name  | qty | note  |
------+-----+-------+------
apple | 3   |       |
kiwi  | 12  | green | extra
```
(The header has 3 cells but the longest row has 4, so there is a fourth, empty-header column of width 5.)
