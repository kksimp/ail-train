Working days between dates

The program reads holidays and date-range queries from standard input, one item per line. Dates are written
`YYYY-MM-DD` and are valid only if the year is 1970..2100, the month 1..12 and the day exists in that month
(leap years follow the Gregorian rules). Working days are Monday to Friday that are not holidays.

Line kinds:
- `holiday DATE`: declares a holiday. Holidays apply to every query, wherever the line appears. Duplicates count once.
- `FROM TO`: a query, answered in input order.
- blank lines are ignored.
Anything else (wrong number of fields, or a `holiday` line whose date is invalid) prints `bad line N`, N being the
1-based line number.

For a query print `FROM TO: R` where R is:
- `invalid` if either date is invalid,
- `reversed` if TO is earlier than FROM,
- otherwise the number of working days from FROM to TO, both ends included.
Output for queries and bad lines appears in input order. 2024-12-02 is a Monday.

Example input:
```
2024-12-23 2024-12-27
holiday 2024-12-25
2024-12-02 2024-12-08
2024-02-28 2024-03-01
2025-02-29 2025-03-01
2024-12-09 2024-12-01
holiday 2024-13-01
```
Output:
```
2024-12-23 2024-12-27: 4
2024-12-02 2024-12-08: 5
2024-02-28 2024-03-01: 3
2025-02-29 2025-03-01: invalid
2024-12-09 2024-12-01: reversed
bad line 7
```
