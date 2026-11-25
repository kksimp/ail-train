# Progressive tax brackets

The first line of standard input lists the brackets as space-separated `LIMIT:RATE` items, in increasing order.
LIMIT is the upper edge of the bracket in cents (a positive integer), or `inf` for the last bracket, which must exist
and must be the only one with `inf`. RATE is in basis points (0..10000). Limits must be strictly increasing.
Each later non-blank line is an income in cents (0..100000000000).

Each bracket taxes the part of the income between the previous limit (0 for the first bracket) and its own limit.
The tax of one bracket is `part * RATE / 10000` rounded half up to a whole cent, and the total tax is the sum of the
per-bracket taxes. The effective rate is `tax * 10000 / income` in basis points, rounded half up, printed as a percent
with two decimals (`1234` prints as `12.34%`); for income 0 it is `0.00%`.

Output one line per income: `income I tax T effective R`, with money as `DOLLARS.CENTS`.
An income line that is not an integer or is out of range prints `line K: bad income`, where K is the 1-based line
number in the whole input. Blank lines are skipped. If the bracket line is missing or invalid print only
`error: bad brackets` and read nothing more.

Example, first line `1000000:1000 4000000:2000 inf:3000`, then `2500000` and `5000000`:

    income 25000.00 tax 4000.00 effective 16.00%
    income 50000.00 tax 10000.00 effective 20.00%

(For 25000.00: 10000.00 at 10% is 1000.00 and 15000.00 at 20% is 3000.00.)
