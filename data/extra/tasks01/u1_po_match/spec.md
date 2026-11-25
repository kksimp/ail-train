# purchase order matching

Three-way matching of invoices against orders and receipts. Reads events on stdin, fields separated by single spaces:
- `po PO SKU QTY PRICE`: order line: QTY units (at least 1) of SKU ordered on PO at PRICE cents each (at least 0).
- `recv PO SKU QTY`: QTY units (at least 1) of that line were received (receipts add up).
- `inv INV PO SKU QTY PRICE`: supplier invoice INV bills QTY units (at least 1) at PRICE cents (at least 0).

All other fields are non-empty words; numbers are digits only. Blank lines are ignored but count for line numbers.
Any other line prints `bad K` (K its 1-based line number) and is ignored; so is a second `po` for the same PO and SKU.
A `recv` for a line that has no `po` also prints `bad K`.

Each `inv` prints one line, judged with what has been read so far:
- `INV reject nopo` if there is no order line for that PO and SKU;
- `INV hold qty` if QTY is more than the units received on that line minus the units already matched by earlier
  invoices;
- `INV hold price` if PRICE differs from the order price by more than 2%, that is
  `abs(PRICE - ORDERPRICE) * 100 > ORDERPRICE * 2` (so with an order price of 0 only a price of 0 passes);
- otherwise `INV match AMOUNT`, AMOUNT being QTY times the invoiced PRICE, and QTY counts as matched.
The checks run in the order listed. A held or rejected invoice matches nothing.

After the input print `matched TOTAL` (sum of AMOUNTs) and `held H`, the number of `hold` lines.

Example:
```
po p1 bolt 100 10
recv p1 bolt 60
inv i1 p1 bolt 50 10
inv i2 p1 bolt 50 10
inv i3 p1 bolt 10 11
inv i4 p2 nut 1 1
```
prints
```
i1 match 500
i2 hold qty
i3 hold price
i4 reject nopo
matched 500
held 2
```
