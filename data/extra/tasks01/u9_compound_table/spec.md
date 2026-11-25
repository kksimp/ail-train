# Compound interest table

Read one line from standard input: `PRINCIPAL RATE YEARS`, three integers separated by spaces.
PRINCIPAL is in cents, RATE is the annual rate in basis points (1 basis point = 0.01%), YEARS is a whole number of years.
Interest is compounded once a year. Each year the interest is `balance * RATE / 10000` in cents, rounded half up
(a fraction of exactly one half cent rounds up), and it is added to the balance before the next year starts.

Valid input: PRINCIPAL 0..10000000, RATE 0..2000, YEARS 1..40, exactly three integers on the first line.
Only the first line is read; anything after it is ignored.

Output, for each year 1..YEARS one line, then a total line. Money prints as `DOLLARS.CENTS` with two digits of cents:

    year Y: interest I balance B
    total interest: T

If the input is empty or the first line is invalid (wrong count, not integers, out of range) print the single line
`error: bad input` and nothing else.

Example, input `100000 500 3`:

    year 1: interest 50.00 balance 1050.00
    year 2: interest 52.50 balance 1102.50
    year 3: interest 55.13 balance 1157.63
    total interest: 157.63

(Year 3: 110250 * 500 / 10000 = 5512.5 cents, which rounds up to 5513.)
