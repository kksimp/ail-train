# FIFO cost of goods sold

Reads inventory events on stdin, fields separated by single spaces:
- `buy SKU QTY UNIT`: a new lot of QTY units arrives, each costing UNIT cents.
- `sell SKU QTY`: QTY units are sold, taken from the oldest lots first (first in, first out).

SKU is a non-empty word. QTY is a whole number of at least 1; UNIT is a whole number of at least 0; both digits only.
Blank lines are ignored but count for line numbers. Any other line prints `bad K` (K its 1-based line number).

For a `sell`, the cost of goods sold (COGS) is the sum over the lots used of units taken times that lot's unit cost.
A lot that is only partly used keeps its remaining units at its own unit cost.
- If SKU has at least QTY units in stock, print `sold SKU QTY cogs C` (C in cents) and remove them.
- Otherwise print `short SKU` and change nothing (also for a SKU never bought).

At the end print `stock SKU QTY VALUE` for every SKU with units left (VALUE is the cents still held in its lots), in
ascending SKU byte order, then `cogs TOTAL`, the sum of all COGS printed. With nothing sold the last line is `cogs 0`.

Example:
```
buy A 10 100
buy A 5 120
sell A 12
sell A 4
```
prints (the first sale takes 10 at 100 and 2 at 120; the second finds only 3 left)
```
sold A 12 cogs 1240
short A
stock A 3 360
cogs 1240
```
