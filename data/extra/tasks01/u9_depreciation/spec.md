# Depreciation schedules

Each non-blank line of standard input describes one asset:

    NAME COST SALVAGE LIFE SL
    NAME COST SALVAGE LIFE DB RATE

NAME is a word without spaces, COST and SALVAGE are in cents (0 <= SALVAGE <= COST <= 100000000), LIFE is a whole
number of years (1..30). `SL` is straight line, `DB` is declining balance with RATE a whole percent (1..100).
Lines are numbered 1, 2, ... counting only non-blank lines.

Straight line: the depreciable amount COST - SALVAGE is divided by LIFE; every year gets the quotient rounded down,
and the leftover cents are added one each to the first years (year 1 first).

Declining balance: each year's depreciation is `book * RATE / 100` of the book value at the start of the year, rounded
half up, but never more than book minus SALVAGE. In the final year (year LIFE) the depreciation is whatever is needed to
bring the book value down to SALVAGE exactly.

Output for each valid asset: a header `NAME (SL)` or `NAME (DB RATE%)`, then one line per year:

    year Y: depreciation D book B

where B is the book value at the end of the year. Money prints as `DOLLARS.CENTS`.
An invalid line (wrong field count, non-integer, out of range, unknown method, missing or extra RATE) prints only
`line K: bad input`. Empty input prints nothing.

Example, input `van 100000 10000 3 SL` and `rig 100000 0 2 DB 50`:

    van (SL)
    year 1: depreciation 300.00 book 700.00
    year 2: depreciation 300.00 book 400.00
    year 3: depreciation 300.00 book 100.00
    rig (DB 50%)
    year 1: depreciation 500.00 book 500.00
    year 2: depreciation 500.00 book 0.00
