Read budget and spending records from standard input, one per line: `kind,category,cents`. `kind` (trimmed) is exactly
`budget` or `actual`; `category` (trimmed) is non-empty; `cents` (trimmed) is a non-negative integer. Exactly 3 fields.
Blank lines are ignored. Any other line prints `line N: invalid` (N is the 1-based line number, blank lines counted)
as it is read, and is skipped.

Amounts for the same kind and category add up. After the input print one line per category (any category that appears in
a valid line), in alphabetical (byte) order:
`CATEGORY: budget=B actual=A diff=D used=P% STATUS`
where D = B - A (negative when overspent, written `-12.50`), P = A * 100 / B with integer division (truncating) or
`n/a` (printed as `used=n/a`, with no percent sign) when B is 0, and STATUS is `OVER` if A > B, `UNDER` if A < B, else `MET`.
Then print `total: budget=B actual=A diff=D` over all categories. Money is dollars with two decimals.

Example input:
    budget,food,50000
    actual,food,32050
    actual,fun,1500
Output:
    food: budget=500.00 actual=320.50 diff=179.50 used=64% UNDER
    fun: budget=0.00 actual=15.00 diff=-15.00 used=n/a OVER
    total: budget=500.00 actual=335.50 diff=164.50

With no valid lines print only `total: budget=0.00 actual=0.00 diff=0.00`.
