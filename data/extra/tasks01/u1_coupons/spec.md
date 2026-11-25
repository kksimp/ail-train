# coupon application rules

Reads one shopping cart on stdin, fields separated by single spaces:
- `item NAME CENTS QTY`: QTY units (at least 1) at CENTS cents each (at least 0), whole numbers, digits only.
- `coupon CODE`: the shopper tries a coupon code.

Blank lines are ignored but count for line numbers. Any other line prints `bad K` (K its 1-based line number) and is
otherwise ignored; those lines come first. The subtotal and unit count cover all items, wherever they appear.

Coupons are judged in the order given, against the whole cart:
- `SAVE10`: 10% off the subtotal.
- `SAVE20`: 20% off the subtotal, needs a subtotal of at least 10000.
- `BULK`: 15% off the subtotal, needs at least 10 units in all.
- `FIVER`: 500 off, needs a subtotal of at least 2000.
- `FREESHIP`: free shipping.
Percent coupons are SAVE10, SAVE20 and BULK: only the first accepted one counts. Print one line per coupon:
`CODE ok`, or `CODE rejected WHY` with WHY one of `unknown` (not in the list), `duplicate` (code already accepted),
`conflict` (a percent coupon was already accepted), `minimum` (subtotal too low), `units` (too few units).

Then print `subtotal S`, `discount D`, `shipping H`, `total T`. The percent discount is the subtotal times the
percentage divided by 100, rounded down; FIVER's 500 is added; D is capped at S. Shipping is 599, but 0 if
FREESHIP was accepted or the subtotal (before discounts) is at least 5000. T is `S - D + H`.

Example:
```
item pen 250 4
item pad 1500 2
coupon SAVE10
coupon BULK
coupon FIVER
coupon FIVER
coupon HALF
```
prints
```
SAVE10 ok
BULK rejected conflict
FIVER ok
FIVER rejected duplicate
HALF rejected unknown
subtotal 4000
discount 900
shipping 599
total 3699
```
