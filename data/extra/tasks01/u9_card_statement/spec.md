# Credit card statement

Standard input: the first line is `APR OPENING` where APR is the annual rate in basis points (0..5000) and OPENING is the
opening balance in cents (-1000000..100000000, negative means a credit). Every later non-blank line is a transaction:
`C AMOUNT` is a charge, `P AMOUNT` is a payment, AMOUNT is a positive integer number of cents (1..100000000).
Anything after the amount on a transaction line is a free-text description and is ignored.
A transaction line with another kind, or a missing, non-positive or non-integer amount, is skipped and reported (see below).

Statement rules:
- interest = `OPENING * APR / 120000` in cents, rounded half up, only when OPENING is positive; otherwise 0.
  It is charged on the opening balance only, not on the new transactions.
- new balance = opening + charges - payments + interest.
- minimum payment: 0 if the new balance is 0 or negative; the whole new balance if it is 2500 cents or less;
  otherwise the larger of 2500 and 2% of the new balance rounded up to the next cent.

Output, each money value as `DOLLARS.CENTS` (a leading `-` when negative):

    skipped line K          (one for each bad transaction line, K is the 1-based input line number, printed first, in order)
    opening: X
    charges: X
    payments: X
    interest: X
    new balance: X
    minimum payment: X

If the first line is missing or invalid (not exactly two integers, or out of range) print only `error: bad header`.

Example, input `1800 100000`, `C 5000 books`, `P 20000`, `X 1`:

    skipped line 4
    opening: 1000.00
    charges: 50.00
    payments: 200.00
    interest: 15.00
    new balance: 865.00
    minimum payment: 25.00
