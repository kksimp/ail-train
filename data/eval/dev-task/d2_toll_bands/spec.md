# toll_bands

Write a command-line program that reads trip records from standard input and prints the toll charged for each trip and the grand total.

## Input

Zero or more lines. Each line is either blank (empty or only spaces/tabs; it is ignored but still counts as a line for numbering) or a trip record of exactly two whitespace-separated words:

    HH:MM KM

`HH` and `MM` are each exactly two characters, `KM` is 1 to 6 characters; all of them must consist only of the digits `0`-`9`. `HH` must be 00-23, `MM` must be 00-59. `KM` is the distance in whole kilometres (0 allowed). Lines are numbered from 1.

## Rules

Let `mins = HH*60 + MM`. The band is:
- `night` if mins < 360 (00:00-05:59), rate 5 cents per km
- `peak` if 420 <= mins < 600 (07:00-09:59) or 960 <= mins < 1140 (16:00-18:59), rate 15 cents per km
- `day` otherwise, rate 10 cents per km

The charge in cents is `KM * rate`, but never more than 2500 cents.

## Output

For each valid trip, in input order, print `TIME KM BAND CHARGE` where TIME is the first word exactly as written, KM is the distance as a plain integer (no leading zeros), BAND is the band name, and CHARGE is dollars with exactly two decimals (cents / 100, then a dot, then cents % 100 padded to two digits, e.g. `7.50`, `0.00`, `25.00`).

For each non-blank line that is not a valid trip (wrong number of words, bad time format, non-digit characters, out-of-range hour or minute, KM too long or empty) print `line K: bad` where K is its line number, and carry on.

After all lines print `total T` where T is the sum of all charges in the same dollar format (`total 0.00` when there are no valid trips, including empty input).

## Example

Input:

    07:30 12
    03:15 40
    12:00 5
    bad line here
    18:59 300
    25:00 4

    22:10 0

Output:

    07:30 12 peak 1.80
    03:15 40 night 2.00
    12:00 5 day 0.50
    line 4: bad
    18:59 300 peak 25.00
    line 6: bad
    22:10 0 day 0.00
    total 29.30
