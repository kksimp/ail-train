# leave_accrual

Write a program that reads employee leave records from standard input and prints each employee's leave balance in hours.

## Input

Each line is `NAME,TENURE,TAKEN`: exactly three comma-separated fields. `NAME` is non-empty text. `TENURE` is the number of completed months of service and `TAKEN` is the leave hours already used; both must be non-negative integers written as one or more digits `0`-`9` only (no sign, no spaces). Blank lines are skipped silently. Any other line that does not satisfy these rules is invalid. Lines are numbered from 1, counting blank lines.

## Rules

Leave accrues per month of service at a rate that depends on the month number:
- months 1 to 12 earn 10 hours each,
- months 13 to 60 earn 12 hours each,
- months 61 and later earn 16 hours each.

So `accrued` for a tenure of `t` months is `10*min(t,12) + 12*(min(t,60) - min(t,12)) + 16*max(0, t-60)`.

`raw = accrued - TAKEN`. The balance is `raw`, but never more than 240 (a cap). An employee whose raw exceeds 240 gets the flag `CAPPED`; an employee whose raw is below 0 gets the flag `OVERDRAWN` (the balance is then negative). An employee has at most one flag.

## Output

For each valid line, in input order: `NAME accrued=A taken=T balance=B`, followed by a space and the flag if there is one. For each invalid line print `error: line K: bad record` at its position in the output (K is the line number). After all lines print `employees: N` (the number of valid lines) and `total balance: S` (sum of the balances, which may be negative).

## Example

Input:
```
ann,6,20
bob,30,10
cy,100,0

dee,3,40
eve,x,1
fay,14,200
```

Output:
```
ann accrued=60 taken=20 balance=40
bob accrued=336 taken=10 balance=240 CAPPED
cy accrued=1336 taken=0 balance=240 CAPPED
dee accrued=30 taken=40 balance=-10 OVERDRAWN
error: line 6: bad record
fay accrued=144 taken=200 balance=-56 OVERDRAWN
employees: 5
total balance: 454
```
