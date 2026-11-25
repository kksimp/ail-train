# inventory ledger

Read commands from standard input, one per line (words separated by spaces; blank lines ignored but they count for line numbers). The ledger tracks stock per SKU; every SKU starts unknown.

Commands:
- `receive SKU QTY`: add QTY (at least 1) units; creates the SKU. Prints `SKU: ONHAND`.
- `ship SKU QTY`: remove QTY (at least 1) units. Prints `SKU: ONHAND`.
- `adjust SKU QTY`: set the on-hand count to QTY (0 or more); creates the SKU. Prints `SKU: ONHAND`.
- `stock SKU`: prints `SKU: ONHAND`.
- `low N`: prints the SKUs whose on-hand count is below N, ascending by name, as `SKU ONHAND` lines, or `none` if there are none.
- `report`: one line `SKU ONHAND IN OUT` per SKU in ascending byte order, where IN is the total received and OUT the total shipped (adjust changes neither), then `skus N` with the SKU count.

Errors print `line K: MESSAGE` (K is the 1-based line number) and change nothing:
- `bad command` for an unknown command or wrong word count
- `bad quantity` if QTY (or N) is not an integer in the allowed range
- `unknown SKU` for `ship` or `stock` of a SKU never seen
- `short SKU: have H, need Q` for a `ship` larger than the on-hand count

Example:
```
receive bolt 10
ship bolt 4
ship bolt 9
report
```
prints
```
bolt: 10
bolt: 6
line 3: short bolt: have 6, need 9
bolt 6 10 4
skus 1
```
