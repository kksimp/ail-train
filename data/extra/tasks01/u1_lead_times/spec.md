# supplier lead-time report

Reads purchase order events on stdin, fields separated by single spaces:
- `po SUPPLIER PO DAY`: purchase order PO was placed with SUPPLIER on day number DAY (a whole number, 0 or more).
- `recv PO DAY`: the goods for PO arrived on day DAY.

SUPPLIER and PO are non-empty words, DAY digits only. Blank lines are ignored but count for line numbers. Any other
line prints `bad K` (K its 1-based line number) and is otherwise ignored. So are these, with the same `bad K`: a `po`
whose PO name was used before, a `recv` for a PO never placed, a second `recv` for a PO, and a `recv` on a day before
the PO's order day.

The lead time of a received PO is its receive day minus its order day. After the input, print one line per supplier
that has at least one PO, in ascending byte order of SUPPLIER:

`SUPPLIER received N open M avg A min X max Y`

N is the number of received POs, M the number still open. A is the mean lead time with one decimal, rounded half
up (compute `(20 * sum + N) / (2 * N)` in integers to get tenths, then print `tens.tenths`); X and Y are the least and
greatest lead time. A supplier with no received PO has `avg - min - max -` after `open M`. The `bad` lines come first.
No POs at all prints nothing but the `bad` lines.

Example:
```
po acme p1 3
po acme p2 4
po zed p3 1
recv p1 10
recv p2 9
```
prints
```
acme received 2 open 0 avg 6.0 min 5 max 7
zed received 0 open 1 avg - min - max -
```
