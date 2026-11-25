# zone_fares

Write a command-line program that reads ride records from standard input and prints the fare of each ride and the total.

## Input

Zero or more lines. A blank line (empty, or only spaces/tabs) is ignored but still counts for numbering. Any other line is a ride when it has exactly two whitespace-separated words `FROM TO`, each a single character from `1` to `9` (a zone number). Lines are numbered from 1.

## Rules

- `crossings = |FROM - TO|` (zone boundaries crossed).
- The fare in cents is `240 + 110 * crossings`, plus a surcharge of 50 cents (once, not per end) if FROM is 1 or TO is 1 (city centre).

## Output

For each valid ride, in input order: `FROM->TO xCROSSINGS FARE`, e.g. `3->6 x3 5.70`. FARE is dollars with exactly two decimals (cents divided by 100, a dot, then cents mod 100 padded to two digits).

For each non-blank line that is not a valid ride print `line K: bad` (K is the line number).

At the end print `total T`, where T is the sum of all fares in the same dollar format (`total 0.00` if there are no valid rides, including empty input).

## Example

Input:

    3 6
    1 1
    4 4

    9 1
    2 10
    7 5 3
    5 2

Output:

    3->6 x3 5.70
    1->1 x0 2.90
    4->4 x0 2.40
    9->1 x8 11.70
    line 6: bad
    line 7: bad
    5->2 x3 5.70
    total 28.40
