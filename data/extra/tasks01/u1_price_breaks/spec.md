# price list with quantity breaks

Reads a price list and purchases on stdin, fields separated by single spaces:
- `price SKU MIN UNIT`: from MIN units upward SKU costs UNIT cents each (a quantity break). MIN is at least 1, UNIT at
  least 0, both whole numbers (digits only). A later `price` for the same SKU and MIN replaces the earlier one.
- `buy SKU QTY`: a purchase of QTY units (whole number, at least 1) priced with the price lines read so far.

SKU is a non-empty word. Blank lines are ignored but count for line numbers. Any other line prints `bad K`
(K its 1-based line number) and is otherwise ignored.

The unit price of a purchase is that of the break with the largest MIN that is not above QTY. Print
`SKU QTY @ UNIT = TOTAL` where TOTAL is QTY times UNIT (cents). If SKU has no break at or below QTY (or no price
at all) print `SKU QTY no price`. When a priced purchase has a higher break (the smallest MIN above QTY), append
` next MIN @ UNIT2` for it, with a leading space.

After the input print `total T`, the sum of all TOTALs, with `total 0` if nothing was priced.

Example:
```
price A 1 500
price A 10 450
price A 100 300
buy A 4
buy A 10
buy A 150
buy B 2
```
prints
```
A 4 @ 500 = 2000 next 10 @ 450
A 10 @ 450 = 4500 next 100 @ 300
A 150 @ 300 = 45000
B 2 no price
total 51500
```
