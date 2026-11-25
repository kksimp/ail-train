# returns processing

Reads sales and returns on stdin, fields separated by single spaces:
- `sale ID SKU QTY PRICE`: order ID sold QTY units of SKU at PRICE cents each.
- `return ID SKU QTY` or `return ID SKU QTY damaged`: the customer sends back QTY units from that order line.

ID and SKU are non-empty words. QTY is a whole number of at least 1, PRICE a whole number of at least 0 (digits only).
A second `sale` for an ID and SKU that already has one is a bad line (the first stays). Blank lines are ignored but
count for line numbers. Any other line prints `bad K` (K its 1-based line number) and is otherwise ignored.

A `return` prints one line:
- `reject ID SKU none` if there is no sale for that ID and SKU;
- `reject ID SKU excess` if QTY is more than the units sold minus the units already returned on that line;
- otherwise `refund ID SKU QTY C`, where C is QTY times the sale's PRICE. The units go back to stock unless the
  return said `damaged`.

After the input print `restocked SKU N` for each SKU with N > 0 units put back (ascending SKU byte order), then
`refunds TOTAL`, the sum of all refunds in cents.

Example:
```
sale o1 A 3 250
return o1 A 2
return o1 A 2
return o1 A 1 damaged
return o2 A 1
```
prints
```
refund o1 A 2 500
reject o1 A excess
refund o1 A 1 250
reject o2 A none
restocked A 2
refunds 750
```
