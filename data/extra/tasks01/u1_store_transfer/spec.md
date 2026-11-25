# stock transfer between stores

Reads events on stdin, fields separated by single spaces:
- `stock STORE SKU QTY`: QTY units of SKU are added to STORE's shelves.
- `transfer ID FROM TO SKU QTY`: ship QTY units of SKU from store FROM to store TO under shipment name ID.
- `receive ID`: shipment ID arrives and its units go onto the shelves of its destination store.

QTY is a whole number of at least 1 (digits only); the other fields are non-empty words. Blank lines are ignored but
count for line numbers. Any other line, and a `transfer` that reuses an ID, prints `bad K` (K its 1-based line number)
and is otherwise ignored.

A `transfer` prints one line: `reject ID same` if FROM and TO are the same store; `reject ID short` if FROM holds fewer
than QTY units of SKU; otherwise `ship ID`, and the units leave FROM at once and are in transit. A `receive` prints
`reject ID unknown` if no accepted shipment has that ID, `reject ID done` if it already arrived, else `arrived ID`.

After the input print `shelf STORE SKU Q` for every store and SKU holding Q > 0 units, ascending by store then SKU
(byte order), then `transit ID FROM TO SKU QTY` for each shipment not yet received, in the order shipped.

Example:
```
stock main A 10
transfer t1 main east A 4
transfer t2 main main A 1
transfer t3 east main A 1
receive t1
receive t1
```
prints
```
ship t1
reject t2 same
reject t3 short
arrived t1
reject t1 done
shelf east A 4
shelf main A 6
```
