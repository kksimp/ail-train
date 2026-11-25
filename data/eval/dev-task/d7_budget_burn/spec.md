# budget_burn

Write a program that replays a log of project budget commands from standard input and prints a burn-down report. All money is integer cents and is printed as a plain integer.

## Input

One command per line; fields are separated by exactly one space (the line is split on every single space, so extra spaces create extra, empty fields). Blank lines (zero characters) are skipped silently. Lines are numbered from 1, counting blank lines. The commands:

- `BUDGET NAME CENTS` creates project NAME with that budget and zero spent.
- `SPEND NAME CENTS` adds CENTS to the project's spent.
- `REFUND NAME CENTS` subtracts CENTS from the project's spent.
- `REALLOC SRC DST CENTS` moves CENTS of budget from project SRC to project DST.
- `MONTH` closes one month (no arguments).

`CENTS` is valid only if it is one or more digits `0`-`9` (no sign) with a value of at least 1.

## Rules

Each line is checked in this order, and the first failure is reported and the line has no other effect:
1. the command word is not one of the five above: `unknown command`
2. the wrong number of fields (4 for REALLOC, 1 for MONTH, 3 for the others): `bad arguments`
3. `CENTS` (the last field) is not valid: `bad amount`
4. BUDGET only: a project with that name exists: `duplicate project NAME`
5. SPEND and REFUND only: NAME does not exist: `unknown project NAME`; for REFUND, then CENTS greater than the project's spent: `refund exceeds spend`
6. REALLOC only: SRC does not exist: `unknown project SRC`; DST does not exist: `unknown project DST`; SRC equals DST: `same project`; after the move SRC's budget would be less than the larger of its spent and 1: `insufficient budget`.

Spending may exceed a budget. Project names are case-sensitive.

## Output

For each failing line, as it is read, print `line K: MESSAGE` (K is the line number). After all input print:
1. `months: M` (number of MONTH commands accepted),
2. one line per project in creation order: `NAME budget=B spent=S left=L used=P% STATUS runway=R` where `L = B - S` (may be negative), `P = S * 100 / B` rounded down, and `STATUS` is `OVER` if `S > B`, else `WARN` if `P >= 80`, else `OK`. The runway is in months: let `avg = S / max(M, 1)` (rounded down); if `avg` is 0 then `runway=inf`, else if `L <= 0` then `runway=0`, else `runway=` `L / avg` rounded down.
3. `projects: N budget=TB spent=TS` with the number of projects and the sums of budget and spent over all projects.

## Example

Input:
```
BUDGET web 100000
BUDGET app 50000
SPEND web 30000
MONTH
SPEND web 50000
MONTH
BUDGET web 5
SPEND api 10
REALLOC web app 25000
REALLOC app web 80000
REFUND app 1
SPEND app 55000
LAUNCH x
SPEND app 0
```

Output:
```
line 7: duplicate project web
line 8: unknown project api
line 9: insufficient budget
line 10: insufficient budget
line 11: refund exceeds spend
line 13: unknown command
line 14: bad amount
months: 2
web budget=100000 spent=80000 left=20000 used=80% WARN runway=0
app budget=50000 spent=55000 left=-5000 used=110% OVER runway=0
projects: 2 budget=150000 spent=135000
```
