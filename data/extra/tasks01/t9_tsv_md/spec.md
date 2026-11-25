# tsv_md

Convert tab-separated text from standard input into a markdown table.

Input: lines of fields separated by a tab character. Empty lines are ignored. The first non-empty line is the header and fixes the number of columns N. Every cell is trimmed of leading and trailing spaces.
- A header cell starting with `>` is right-aligned; one starting with `^` is centered; otherwise left-aligned. The marker is removed from the header text (then the cell is trimmed again).
- A data row with fewer than N cells is padded with empty cells; extra cells beyond N are dropped.
- In every cell, each `|` is replaced by `\|`.

Output:
- Header line: `| ` + cells joined with ` | ` + ` |`.
- Alignment line: one entry per column joined with ` | ` inside the same outer bars: `---` for left, `---:` for right, `:---:` for centered.
- One line per data row, formatted like the header line.
- With no non-empty input line, print nothing.

Example input (`<TAB>` stands for a tab):
```
item<TAB>>price<TAB>^ok
a|b<TAB>3
pen<TAB>12<TAB>yes<TAB>dropped
```
Example output:
```
| item | price | ok |
| --- | ---: | :---: |
| a\|b | 3 |  |
| pen | 12 | yes |
```
