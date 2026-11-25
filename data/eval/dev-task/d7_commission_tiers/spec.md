# commission_tiers

Write a program that reads sales and returns from standard input and prints each sales rep's commission under a tiered plan.

## Input

Each line is `REP,AMOUNT` with exactly two comma-separated fields. `REP` is non-empty text. `AMOUNT` is an integer number of cents: an optional `-` followed by one or more digits `0`-`9` (no `+`, no spaces); negative amounts are returns. Blank lines are skipped silently. Any other line is invalid. Lines are numbered from 1, counting blank lines.

## Rules

- A rep's `total` is the sum of all their valid amounts (it may be negative).
- Commission is computed on `base = max(0, total)` with marginal tiers, each tier's commission rounded down separately:
  - the first 1000000 cents of base earn 5% (500 basis points),
  - the part of base above 1000000 and up to 5000000 earns 8% (800 basis points),
  - the part of base above 5000000 earns 12% (1200 basis points).
  The commission of a portion `p` at `b` basis points is `p * b / 10000` rounded down (integer division). The rep's commission is the sum over the three tiers.
- Money is printed with a leading `-` if negative, then `$`, the whole dollars, `.`, and exactly two digits of cents, computed from the absolute value in cents (for example 123456 is `$1234.56`, -5 is `-$0.05`).

## Output

First, for every invalid line, in input order, print `error: line K: bad sale` (K is the line number). Then print one line per rep, sorted by commission descending, ties broken by rep name ascending (plain byte order): `REP total=T commission=C` with T and C in the money format. Finally print `reps: N` (number of reps with at least one valid line) and `payout: P` (the sum of all commissions, money format).

## Example

Input:
```
ann,1500000
bob,300000
ann,-200000
cy,7000000
bob,x

dee,0
bob,300000
```

Output:
```
error: line 5: bad sale
cy total=$70000.00 commission=$6100.00
ann total=$13000.00 commission=$740.00
bob total=$6000.00 commission=$300.00
dee total=$0.00 commission=$0.00
reps: 4
payout: $7140.00
```
