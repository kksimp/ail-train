# reorder point report

Reads item lines on stdin: `item NAME ONHAND DAILY LEAD SAFETY TARGET`, fields separated by single spaces.
NAME is a non-empty word; the other five fields are whole numbers (digits only, 0 allowed): units on hand, average
units sold per day, supplier lead time in days, safety stock, and the stock level to order up to.

A later line for a NAME replaces the earlier one. Blank lines are ignored but count for line numbers. Any other line
prints `bad K` (K its 1-based line number) and is ignored; those lines come first, in input order.

For each item the reorder point is `DAILY * LEAD + SAFETY`. An item needs a reorder when ONHAND is at or below its
reorder point. The order quantity is `TARGET - ONHAND`, or 0 if that is negative. The shortfall is
`reorder point - ONHAND`.

Print one line per item that needs a reorder, most urgent first (largest shortfall first, ties by NAME ascending in
byte order): `NAME onhand O point P short S order Q`. Then print `reorder N of M` where N is the number of lines
printed and M the number of distinct items. With no items print `reorder 0 of 0`.

Example:
```
item bolt 20 5 4 10 100
item nut 90 5 4 10 100
item gear 0 1 1 0 6
```
prints
```
bolt onhand 20 point 30 short 10 order 80
gear onhand 0 point 1 short 1 order 6
reorder 2 of 3
```
