A currency converter with a fixed rate table. Each currency has a rate: how many units of it equal 1 USD, in
ten-thousandths: USD 10000, EUR 9200, GBP 7900, JPY 1500000, CAD 13600. All amounts, in every currency, are integer
hundredths ("cents") and are shown as `D.CC`.

Read lines from standard input; blank lines are ignored; fields are separated by runs of spaces.
1. `AMOUNT FROM TO`: convert AMOUNT (non-negative integer cents) from currency FROM to TO. The result is
   AMOUNT * rate(TO) / rate(FROM) rounded half up to a whole cent, computed as
   (2 * AMOUNT * rate(TO) + rate(FROM)) / (2 * rate(FROM)) with integer division. Print `X FROM = Y TO`.
2. `table AMOUNT FROM`: print `X FROM:` and then one line `  CODE: Y` for every currency, in alphabetical order, with
   the AMOUNT converted to that currency (the same formula).
A line with a wrong number of words or a bad AMOUNT (not only digits) prints `line N: invalid` (N is the 1-based line
number, blank lines counted). A currency code (case-sensitive) not in the table prints `line N: unknown currency`.
Bad format is checked first. After all lines print `total CODE: Y` for each target currency used by a valid
`AMOUNT FROM TO` line, in alphabetical order, where Y is the sum of its results (table lines are not counted).

Example input:
    12345 EUR USD
    10000 USD JPY
Output:
    123.45 EUR = 134.18 USD
    100.00 USD = 1500.00 JPY
    total JPY: 1500.00
    total USD: 134.18

No valid conversions means no total lines.
