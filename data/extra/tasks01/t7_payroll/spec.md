Read payroll records from standard input, one per line: `name,hours,rate_cents` (whole hours worked, hourly rate in
integer cents). Blank lines are ignored. A line is invalid if it does not have exactly 3 comma-separated fields, the
trimmed name is empty, or hours or rate is not a non-negative integer (after trimming). For an invalid line print
`line N: invalid` (N is the 1-based line number, blank lines counted) and otherwise skip it.

For a valid record: regular hours are the first 40 hours, overtime hours are those above 40. Regular pay is
regular_hours * rate. Overtime pay is overtime_hours * rate * 3 / 2 using integer division (truncating). Gross is the sum.
Print `NAME: reg=R ot=O gross=G` in input order, then a final line `total: K employees gross=T`, where K is the number
of valid records. Money is shown as dollars with two decimals (`12345` cents -> `123.45`).

Example input:
    ann,45,2000
    bob,38,1550
Output:
    ann: reg=800.00 ot=150.00 gross=950.00
    bob: reg=589.00 ot=0.00 gross=589.00
    total: 2 employees gross=1539.00

Empty input prints `total: 0 employees gross=0.00`.
