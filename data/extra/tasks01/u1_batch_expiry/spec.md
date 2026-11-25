# batch expiry report

Reads events on stdin, fields separated by single spaces. Days are whole day numbers (digits only, 0 or more).
- `lot SKU LOT QTY EXP`: a batch LOT of SKU with QTY units (at least 1) that expires at the end of day EXP.
- `asof DAY`: sets today's date to DAY (initially 0).
- `sell SKU QTY`: sell QTY units (at least 1) from batches of SKU that have not expired (EXP is at least today),
  using the batch that expires soonest first (ties: LOT in ascending byte order).

SKU and LOT are non-empty words. Blank lines are ignored but count for line numbers. Any other line, and a `lot`
whose SKU and LOT were used before, prints `bad K` (K its 1-based line number) and is otherwise ignored.

A `sell` prints `sold SKU QTY` when enough unexpired units exist and takes them; otherwise `short SKU` and nothing
changes. Other lines print nothing.

After the input print the state for the final value of today (call it T), every batch that still has units:
- `expired SKU LOT QTY EXP` for batches with EXP below T,
- then `soon SKU LOT QTY EXP` for batches with EXP from T up to T + 7,
each group sorted by EXP, then SKU, then LOT. Finally `expired units N`, the units in expired batches
(`expired units 0` if none). Lines of the sells come first, in input order.

Example:
```
lot milk m1 10 5
lot milk m2 6 9
lot egg e1 3 40
asof 6
sell milk 12
sell milk 5
asof 10
```
prints
```
short milk
sold milk 5
expired milk m1 5 5
soon milk m2 1 9
expired units 5
```
