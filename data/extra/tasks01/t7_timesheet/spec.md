Read shifts from standard input, one per line: `name,date,start,end`. Blank lines are ignored. `date` is `YYYY-MM-DD`
(4 digits, 2 digits 01-12, 2 digits 01-31); `start` and `end` are `HH:MM` on a 24-hour clock (2 digits 00-23, 2 digits
00-59). Fields are trimmed; the name must be non-empty; there must be exactly 4 fields; `end` must be later than `start`.
Any other line prints `line N: invalid` (N is the 1-based line number, blank lines counted) as it is read, and is skipped.

Paid minutes for a shift are end minus start in minutes, minus 30 minutes of unpaid break if the shift is longer than
360 minutes. After reading all input print, for each name in alphabetical (byte) order,
`NAME: H:MM over D days (S shifts)` where H:MM is total paid time (minutes zero-padded to 2 digits, hours not padded),
D the number of distinct dates the person worked and S the number of valid shifts. Then print `all: H:MM`, the total of
everybody.

Example input:
    ann,2024-03-01,09:00,17:30
    ann,2024-03-01,18:00,19:00
    bob,2024-03-02,08:00,12:00
Output:
    ann: 9:00 over 1 days (2 shifts)
    bob: 4:00 over 1 days (1 shifts)
    all: 13:00

With no valid shifts print only `all: 0:00` (after any invalid-line messages).
