Minutes-per-category time log

The program reads a work log and reports how many minutes went to each category.

Each non-blank line is `DATE CATEGORY DURATION`:
- DATE is text of the form `YYYY-MM-DD` (compared as text, never interpreted).
- CATEGORY is a word without spaces; categories are case-insensitive and reported in lower case.
- DURATION is `XhYm`, `Xh` or `Ym` (for example `1h30m`, `2h`, `45m`), where X and Y are non-negative integers;
  Y may exceed 59 (`0h90m` is 90 minutes). The total must be at least 1 minute.
A line with the wrong number of fields, a malformed date (not 4-2-2 digits separated by `-`) or a bad duration prints
`bad line N` (1-based line number) and is not counted. These messages come first, in input order.

Then print the report: one line per category, ordered by minutes (largest first), ties by name (byte order):
`CATEGORY MINUTESm (HhMMm) P%` where H = MINUTES / 60, MM = MINUTES mod 60 written with two digits, and P = 100 * MINUTES / TOTAL
rounded down (integer division), TOTAL being the minutes over all valid lines.
Then `total TOTALm (HhMMm)` and `busiest DATE MINUTESm`, the date with the most minutes (ties: smallest date text).
With no valid lines print only `no entries` after any `bad line` messages.

Example input:
```
2024-05-01 Dev 1h30m
2024-05-01 meet 45m
2024-05-02 dev 2h
2024-05-02 Admin 0h20m
2024-05-03 dev 1h5
2024-05-3 dev 10m
```
Output:
```
bad line 5
bad line 6
dev 210m (3h30m) 76%
meet 45m (0h45m) 16%
admin 20m (0h20m) 7%
total 275m (4h35m)
busiest 2024-05-02 140m
```
