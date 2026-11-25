# Price change report

Each non-blank line of standard input is `ITEM OLD NEW`: an item name (one word) and its old and new price in cents
(integers 0..1000000000). Lines are numbered by position in the input (blank lines count).

The percentage change in basis points is `(NEW - OLD) * 10000 / OLD`, rounded half away from zero (a fraction of exactly
one half moves away from zero, so -0.5 becomes -1 and 0.5 becomes 1). It prints as a signed percent with two decimals:
`+12.34%`, `-0.50%`, and `0.00%` when it is zero. If OLD is 0 the change is `n/a`.

Output: first one `line K: bad line` for every invalid line (wrong field count, non-integer, out of range), in order.
Then the valid items sorted by change, largest increase first; ties are ordered by item name (byte order); items with
`n/a` come last, also ordered by name. Each item prints as

    ITEM OLD -> NEW CHANGE

with OLD and NEW as `DOLLARS.CENTS`. Last, a summary line `up U, down D, same S, n/a N` where an item is up when NEW > OLD,
down when NEW < OLD, same when equal (and OLD > 0), and n/a when OLD is 0. With no valid items print only the summary.

Example, input `tea 250 275`, `jam 400 380`, `ice 0 99`, `oat 1000 1000`:

    tea 2.50 -> 2.75 +10.00%
    oat 10.00 -> 10.00 0.00%
    jam 4.00 -> 3.80 -5.00%
    ice 0.00 -> 0.99 n/a
    up 1, down 1, same 1, n/a 1
