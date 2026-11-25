Deadline tracker with overdue report

The program reads a reference date and a list of tasks, and prints an overdue and a due-soon report.

Line 1: `today YYYY-MM-DD`. If it is missing or not a valid date, print `no today line` and stop.
Every other non-blank line is a task: `DATE STATUS NAME`, where DATE is `YYYY-MM-DD`, STATUS is `open` or `done`,
and NAME is the rest of the line (it may contain spaces, and must not be empty). A date is valid if the month is 1..12 and
the day exists in that month (leap years follow the Gregorian rules, years 1970..2100). An invalid line prints
`bad line N` (1-based line number) and is not counted.

Only `open` tasks appear in the reports. Let `days` be the number of days from `today` to the task's date.
- OVERDUE: open tasks with days < 0, listed by days overdue (largest first), ties by name (byte order).
  Each line is `  K days: NAME (DATE)` where K = -days; use `1 day` when K is 1.
- DUE SOON: open tasks with 0 <= days <= 3, listed by days ascending, ties by name. Each line is `  K days: NAME (DATE)`
  with K = days, again `1 day` for 1, and `today` instead of `0 days`.
An empty section prints `  none`. Finally print `done D open O overdue V` (counts of valid tasks).

Example input:
```
today 2024-03-10
2024-03-01 open write report
2024-03-12 open pay rent
2024-02-20 done old task
2024-03-10 open call bank
2024-03-09 open file taxes
oops
```
Output:
```
OVERDUE
  9 days: write report (2024-03-01)
  1 day: file taxes (2024-03-09)
DUE SOON
  today: call bank (2024-03-10)
  2 days: pay rent (2024-03-12)
done 1 open 4 overdue 2
bad line 7
```
`bad line` messages are printed after the final summary line, in input order.
