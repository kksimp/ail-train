# Tip splitting

Each non-blank line of standard input is one bill: `TOTAL PERCENT PEOPLE MODE`.
TOTAL is the bill in cents (0..100000000), PERCENT the tip percentage (0..100), PEOPLE the number of diners (1..20),
MODE is the tip rounding rule: `half`, `up` or `down` (lower case).

The tip is `TOTAL * PERCENT / 100` in cents, rounded to a whole cent by MODE:
`down` drops the fraction, `up` rounds any fraction up, `half` rounds a fraction of exactly one half or more up.
The grand total is TOTAL plus the tip. It is split into PEOPLE shares: everyone pays the grand total divided by
PEOPLE rounded down, and the leftover cents are given one each to the first people in order (person 1 first).

Bills are numbered 1, 2, ... counting only non-blank lines. For each bill print:

    bill K: tip T total G
    person I: S             (one line per diner, I from 1)

Money prints as `DOLLARS.CENTS`. A line with the wrong number of fields, a non-integer number, a value out of range
or an unknown mode prints only `bill K: bad input`. Empty input prints nothing.

Example, input `10001 15 3 half`:

    bill 1: tip 15.00 total 115.01
    person 1: 38.34
    person 2: 38.34
    person 3: 38.33

(The tip is 1500.15 cents, which rounds to 1500; the total 11501 splits as 3833 with 2 cents left over.)
