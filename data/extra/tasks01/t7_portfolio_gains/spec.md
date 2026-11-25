Read portfolio events from standard input, one per line, fields separated by runs of spaces:
`BUY SYM QTY PRICE`, `SELL SYM QTY PRICE` or `MARK SYM PRICE`. QTY is an integer >= 1, PRICE (cents per share) an integer
>= 0, both made only of digits. Blank lines are ignored. Any other line prints `line N: invalid` (N is the 1-based line
number, blank lines counted).

Holdings use the average-cost method per symbol. BUY adds QTY shares and QTY * PRICE to the cost basis. SELL of more
shares than held (including a symbol never bought) prints `line N: oversell` and changes nothing. Otherwise a SELL removes
shares: cost removed = basis * QTY / held (integer division, held being the shares before the sale); the realized gain
increases by QTY * PRICE minus cost removed; the basis drops by the cost removed. MARK sets the current price of the
symbol. Every symbol seen in a valid line gets a report entry (even if now fully sold).
The current price of a symbol is its last MARK, else the price of its latest BUY or SELL, else 0.

After all lines print, for each symbol in alphabetical (byte) order,
`SYM: qty=Q cost=C value=V unrealized=U realized=R` where value = Q * current price and unrealized = value - cost.
Then `total: cost=C value=V unrealized=U realized=R` summed over all symbols. Money is dollars with two decimals;
negative amounts are written `-12.50`.

Example input:
    BUY AAA 10 1000
    SELL AAA 4 1500
    MARK AAA 1200
Output:
    AAA: qty=6 cost=60.00 value=72.00 unrealized=12.00 realized=20.00
    total: cost=60.00 value=72.00 unrealized=12.00 realized=20.00

No valid lines prints only a total line of zeros.
