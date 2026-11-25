Read plan changes from standard input, one per line: `customer,old_plan,new_plan,day,cycle_days`. Blank lines are
ignored. Fields are trimmed. Plans and monthly prices in cents: `basic` 1000, `pro` 2500, `team` 6000. `cycle_days` is an
integer 28 to 31 and `day` an integer from 1 to cycle_days (digits only): the new plan applies from that day onward,
the old plan was in force on the days before it. The customer must be non-empty and there must be exactly 5 fields. Any other line
prints `line N: invalid` (N is the 1-based line number, blank lines counted) and is skipped.

The old plan is charged for (day - 1) days and the new plan for (cycle_days - day + 1) days. A part is
price * days / cycle_days rounded half up, computed as (price * days * 2 + cycle_days) / (2 * cycle_days) with integer
division. Print `CUSTOMER: old=X new=Y total=T delta=D` where X and Y are the two parts, T = X + Y and
D = T - old plan price (negative for a downgrade, written `-12.50`). Money is dollars with two decimals.
After the input print `billed: S` (the sum of all T) and `net change: N` (the sum of all D).

Example input:
    ann,basic,pro,11,30
Output:
    ann: old=3.33 new=16.67 total=20.00 delta=10.00
    billed: 20.00
    net change: 10.00

With no valid lines print `billed: 0.00` and `net change: 0.00`.
