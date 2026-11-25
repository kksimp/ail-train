Recurring event expansion

The program reads recurring event rules and prints every occurrence in date order.

Each non-blank line is a rule: `NAME START FREQ COUNT`
- NAME is a word without spaces.
- START is a date `YYYY-MM-DD`, valid if the year is 1970..2100, the month 1..12 and the day exists (Gregorian leap years).
- FREQ is `daily`, `weekly`, `monthly` or `yearly`.
- COUNT is an integer from 1 to 20: the number of occurrences, the first being START itself.
A rule that does not fit prints `bad line N` (1-based line number) and is ignored.

Occurrence k (k = 0, 1, ...) is: START plus k days (daily), plus 7k days (weekly), the same day of the month k months later (monthly),
or the same month and day k years later (yearly). When the month or year step lands on a day that does not exist
(for example the 31st in a 30-day month, or 29 February in a non-leap year) the occurrence falls on the last day of that
month instead. Each occurrence is computed from START, not from the previous occurrence, so a monthly event on the 31st
returns to the 31st whenever the month has one.

Output: every occurrence of every valid rule as `DATE NAME`, ordered by date, then by name (byte order), then by rule
order. Finish with `total T`, the number of occurrences printed. Years of occurrences may exceed 2100.

Example input:
```
rent 2024-01-31 monthly 4
gym 2024-02-26 weekly 3
leap 2024-02-29 yearly 2
bad 2024-02-30 daily 1
```
Output:
```
2024-01-31 rent
2024-02-26 gym
2024-02-29 leap
2024-02-29 rent
2024-03-04 gym
2024-03-11 gym
2024-03-31 rent
2024-04-30 rent
2025-02-28 leap
total 9
bad line 4
```
`bad line` messages come after the total line, in input order.
