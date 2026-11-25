# Invoice aging buckets

The first line of standard input is the report date `ASOF` as `YYYY-MM-DD`. Every later non-blank line is an invoice:
`ID AMOUNT DUE` where ID is a word, AMOUNT is the open amount in cents (an integer 1..1000000000) and DUE is the due
date `YYYY-MM-DD`.

A date is valid when it has exactly the shape `YYYY-MM-DD` (4, 2 and 2 digits), the year is 1900..2100, the month is
1..12 and the day exists in that month (leap years follow the Gregorian rules: divisible by 4, except centuries not
divisible by 400).

The days overdue of an invoice is ASOF minus DUE in days (zero or negative means not yet overdue). Buckets:

    current     days overdue <= 0
    1-30        1..30
    31-60       31..60
    61-90       61..90
    90+         91 or more

Output five bucket lines in that order, then the grand total:

    LABEL: N invoices, TOTAL
    total: N invoices, TOTAL

N is the number of invoices (always the word `invoices`, even for 1), TOTAL the sum of amounts as `DOLLARS.CENTS`.
An invalid invoice line (wrong field count, bad amount, bad date) is reported before the table as
`line K: bad invoice`, K being its 1-based line number in the input, and is left out. Blank lines are skipped.
If the first line is not a valid date print only `error: bad date`.

Example: ASOF `2024-03-31`, invoices `a 10000 2024-03-01`, `b 5050 2024-04-02`, `c 1 2024-03-30`:

    current: 1 invoices, 50.50
    1-30: 2 invoices, 100.01
    31-60: 0 invoices, 0.00
    61-90: 0 invoices, 0.00
    90+: 0 invoices, 0.00
    total: 3 invoices, 150.51
