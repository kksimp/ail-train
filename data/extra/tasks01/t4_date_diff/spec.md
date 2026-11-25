# Date difference

Each non-blank input line should hold two dates separated by whitespace: `START END`. A date is written
`YYYY-MM-DD`: exactly four, two and two ASCII digits, a real calendar date in the proleptic Gregorian calendar
(leap years: divisible by 4, except centuries not divisible by 400), year 0001 to 9999.

For each non-blank line print the number of days from START to END (END minus START, negative if END is earlier),
or `invalid` if the line does not have exactly two tokens or either token is not a valid date.
Blank lines (empty or only whitespace) are skipped.

Example input:
    2024-01-01 2024-03-01
    2000-03-01 1999-03-01
    2023-02-29 2023-03-01
    2020-05-05

Example output:
    60
    366
    invalid
    invalid

Empty input prints nothing.
