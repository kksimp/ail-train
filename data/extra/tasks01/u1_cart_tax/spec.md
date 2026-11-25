# cart totals with mixed tax rates

Reads a cart on stdin, fields separated by single spaces:
- `tax CAT BPS`: category CAT is taxed at BPS basis points (hundredths of a percent; 0 to 10000, digits only).
  A later `tax` for the same CAT replaces the earlier one. Tax lines apply to the whole cart wherever they appear.
- `item NAME CAT CENTS QTY`: QTY units (at least 1) of NAME at CENTS cents each (at least 0), in category CAT.

NAME and CAT are non-empty words. Blank lines are ignored but count for line numbers. Any other line prints
`bad K` (K its 1-based line number) and is otherwise ignored; those lines come first, in input order.

For each item, in input order, print `NAME net N tax T`. N is CENTS times QTY. T is the tax on that line alone:
`N * BPS / 10000` rounded to the nearest cent, halves rounding up (that is `(N * BPS + 5000) / 10000` in integers).
An item whose category has no `tax` line pays 0 and has ` no rate` added at the end of its line.

Then, for each category used by at least one item, in ascending byte order, print `cat CAT net N tax T` with the
sums of its lines. Finally print `net N`, `tax T`, `total N+T` (as one number) for the whole cart.
An empty cart prints `net 0`, `tax 0`, `total 0` on three lines.

Example:
```
tax food 500
tax gadget 2000
item apple food 99 3
item phone gadget 19999 1
item gift misc 100 2
```
prints
```
apple net 297 tax 15
phone net 19999 tax 4000
gift net 200 tax 0 no rate
cat food net 297 tax 15
cat gadget net 19999 tax 4000
cat misc net 200 tax 0
net 20496
tax 4015
total 24511
```
