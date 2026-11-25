# Mortgage comparison

Each non-blank line of standard input is one loan offer: `NAME PRINCIPAL RATE YEARS`. NAME is one word, PRINCIPAL is in
cents (1..500000000), RATE the annual rate in basis points (0..3000), YEARS the term (1..40). Offers are numbered by
their position in the input (blank lines count). An invalid line (wrong field count, non-integer, out of range) is
reported first as `line K: bad offer` and left out.

The loan is repaid in N = 12 * YEARS monthly payments. Each month the interest is `balance * RATE / 120000` in cents,
rounded half up, on the balance at the start of the month; it is added to the balance and then one payment is taken off.
The level payment is the smallest whole number of cents such that the balance is fully repaid within N months.
The last payment is smaller if needed (it just clears the remaining balance plus interest); the schedule stops when the
balance reaches zero. Total interest is the sum of the monthly interest amounts, total paid is the sum of all payments.

Then print the offers ranked by total interest, lowest first (ties keep input order), one line each:

    R. NAME payment P months M interest I total T

R is the rank from 1, P the level payment, M the number of payments actually made, I the total interest, T the total paid,
all money as `DOLLARS.CENTS`. Finally print `spread: X` where X is the highest total interest minus the lowest.
With no valid offers print only `spread: 0.00`.

Example, input `quick 120000 0 1` and `slow 120000 0 2`:

    1. quick payment 100.00 months 12 interest 0.00 total 1200.00
    2. slow payment 50.00 months 24 interest 0.00 total 1200.00
    spread: 0.00
