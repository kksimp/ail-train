# cycle_count

Write a program that reads warehouse cycle-count records from standard input and reports the stock variances and their money value.

## Input

Each line is `SKU,SYSTEM,COUNTED,COST` with exactly four comma-separated fields: `SKU` is any text, `SYSTEM` is the quantity on the books, `COUNTED` is the quantity found on the shelf, and `COST` is the unit cost in integer cents. The three numeric fields are valid only if each is an optional `-` followed by one or more digits `0`-`9` (no spaces, no `+`). Any line that does not have exactly four fields, or has an invalid numeric field, is ignored silently (this includes blank lines).

## Rules

- The variance of a record is `COUNTED - SYSTEM`. Its value is `variance * COST` in cents.
- Records with variance 0 are not listed.
- Money is printed as a sign (`+` or `-`; `+` for zero), then `$`, then whole dollars, a `.`, and exactly two digit cents, computed from the absolute value in cents (for example 450 is `+$4.50`, -5 is `-$0.05`).
- The variance quantity is printed with an explicit sign (`+3`, `-2`).

## Output

For every listed record, in input order: `SKU VARIANCE VALUE` separated by single spaces. Then two lines: `net: M` where M is the money format of the sum of all values, and `gross: M` where M is the money format of the sum of the absolute values of all values. These two lines are always printed, even when nothing is listed (then both are `+$0.00`).

## Example

Input:
```
A100,10,8,250
B200,5,5,999
C300,0,12,35
bad line
D400,7,x,100
E500,3,2,-40
```

Output:
```
A100 -2 -$5.00
C300 +12 +$4.20
E500 -1 +$0.40
net: -$0.40
gross: +$9.60
```
