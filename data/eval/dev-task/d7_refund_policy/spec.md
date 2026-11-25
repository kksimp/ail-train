# refund_policy

Write a program that reads refund requests from standard input, decides each one under a store policy, and prints the decisions and totals. All money is integer cents, printed as plain integers.

## Input

Each line is a request `ID,CATEGORY,PAID,DAYS,CONDITION` with exactly five comma-separated fields:
- `ID`: non-empty text.
- `CATEGORY`: any text (exact, case-sensitive; only `electronics`, `clothing`, `grocery` and `software` are known categories).
- `PAID`: cents paid, valid only as one or more digits `0`-`9` with a value of at least 1.
- `DAYS`: days since purchase, valid only as one or more digits `0`-`9` (zero allowed).
- `CONDITION`: exactly `sealed`, `opened` or `defective`.

A line breaking any of these rules (including a wrong field count or an empty ID) is malformed. Blank lines (zero characters) are skipped silently. Lines are numbered from 1, counting blank lines.

## Rules

The return window in days is: electronics 30, clothing 60, grocery 7, software 14. A well-formed request is decided by the first rule that applies:
1. Unknown category: `REJECT unknown category`.
2. Condition `defective`: if `DAYS` is more than twice the window, `REJECT window expired`; otherwise the refund is the full `PAID`, paid as cash.
3. `DAYS` greater than the window: `REJECT window expired`.
4. Condition `opened`: for software or grocery, `REJECT opened software` or `REJECT opened grocery`; for electronics a restocking fee of 15% of `PAID` (rounded down) is kept, for clothing 10% (rounded down); the refund is `PAID` minus the fee.
5. Condition `sealed`: the refund is the full `PAID`.

For rules 4 and 5 the refund is paid as cash if `DAYS * 2 <= window`, otherwise as store credit. Finally, any refund (cash or credit) greater than 50000 is not approved but sent to review.

## Output

For each malformed line print `line K: malformed request`. For each request print one line, in input order: `ID APPROVE cash AMOUNT`, `ID APPROVE credit AMOUNT`, `ID REVIEW AMOUNT`, or `ID REJECT REASON`. After all input print exactly four lines:
- `approved: N cash=C credit=D` (the number of approved requests and the sums of cash and credit refunds),
- `review: N amount=A` (the number of reviewed requests and the sum of their refunds),
- `rejected: N`,
- `malformed: N`.

## Example

Input:
```
R1,electronics,20000,10,sealed
R2,electronics,20000,10,opened
R3,clothing,5999,45,sealed
R4,grocery,899,3,opened
R5,software,4900,20,defective
R6,software,4900,29,defective
R7,toys,1000,1,sealed
R8,electronics,90000,5,defective
R9,clothing,3000,x,sealed
R10,clothing,3000,61,sealed

R11,software,2500,14,opened
```

Output:
```
R1 APPROVE cash 20000
R2 APPROVE cash 17000
R3 APPROVE credit 5999
R4 REJECT opened grocery
R5 APPROVE cash 4900
R6 REJECT window expired
R7 REJECT unknown category
R8 REVIEW 90000
line 9: malformed request
R10 REJECT window expired
R11 REJECT opened software
approved: 4 cash=41900 credit=5999
review: 1 amount=90000
rejected: 5
malformed: 1
```
