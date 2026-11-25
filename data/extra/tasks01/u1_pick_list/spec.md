# warehouse pick list by bin

Reads warehouse lines on stdin, fields separated by single spaces:
- `loc SKU BIN`: SKU is stored in bin BIN (a later `loc` for the same SKU replaces the earlier one).
- `pick ORDER SKU QTY`: order ORDER needs QTY (a whole number, at least 1, digits only) units of SKU.

SKU, ORDER and BIN are non-empty words made of `A-Z`, `0-9` and `-`. Blank lines are ignored but count for line
numbers. Any other line (unknown word, wrong field count, bad QTY) prints `bad K` (K its 1-based line number) and
is otherwise ignored; those lines come first in the output, in input order.

After reading everything, print the pick list: all picks of the same SKU are added together, and the SKUs are grouped
by their final bin. A SKU with no `loc` goes in the pseudo bin `NOBIN`, which comes last; other bins are in ascending
byte order. For each bin print `bin BIN`, then one line `  SKU QTY` (two leading spaces) per SKU in ascending order.
Finally print `lines N units M`: the number of SKU lines printed and the total units. With no picks print only
`lines 0 units 0` (after any `bad` lines).

Example:
```
loc A1 B-02
loc C9 B-01
pick o1 A1 2
pick o2 C9 1
pick o3 A1 3
pick o3 Z 4
```
prints
```
bin B-01
  C9 1
bin B-02
  A1 5
bin NOBIN
  Z 4
lines 3 units 10
```
