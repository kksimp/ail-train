# backorder fulfilment

Reads a log of warehouse events on stdin, one per line, fields separated by single spaces:
- `stock SKU QTY`: QTY units arrive on hand.
- `order ID SKU QTY`: ship as many units as are on hand (at most QTY); the rest is backordered.
- `restock SKU QTY`: QTY units arrive, then open backorders for that SKU are filled, oldest first, from the stock.

QTY is a whole number of at least 1 (digits only). SKU and ID are non-empty words. Blank lines are ignored but count
for line numbers. A line that is anything else (unknown word, wrong field count, bad QTY) prints `bad K`, K being its
1-based line number, and changes nothing.

Output, in order while reading:
- for `order`: `ID shipped S backorder B` (S shipped now, B left open; B may be 0). A backordered order joins the queue.
- for `restock`: one line `fill ID N` for each backorder that received N > 0 units (an order may be filled in parts).

After the input, print `on-hand SKU Q` for every SKU ever stocked or ordered, sorted by SKU (byte order), then
`open ID SKU LEFT` for each backorder still unfilled, in the order the orders arrived.

Example:
```
stock A 5
order o1 A 8
restock A 2
order o2 B 1
```
prints
```
o1 shipped 5 backorder 3
fill o1 2
o2 shipped 0 backorder 1
on-hand A 0
on-hand B 0
open o1 A 1
open o2 B 1
```
Empty input prints nothing.
