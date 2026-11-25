# d5_unit_chain

Write a command-line program that reads length conversion requests from standard input and prints each converted value.

## Input

Zero or more lines. Lines are numbered from 1. A line with no words (empty or only whitespace) is ignored, but still counts in the numbering. Words are separated by one or more spaces or tabs.

A valid request has exactly three words: `VALUE FROM TO`.

- `VALUE` is one to nine ASCII digits (a non-negative integer; leading zeros are allowed, no sign, no decimal point).
- `FROM` and `TO` are unit names from this table, which gives the size of each unit in micrometres (`um`):

| unit | micrometres |
|------|-------------|
| um | 1 |
| mm | 1000 |
| cm | 10000 |
| m | 1000000 |
| km | 1000000000 |
| in | 25400 |
| ft | 304800 |
| yd | 914400 |
| mi | 1609344000 |

Unit names are matched exactly (lower case only).

## Rules

The conversion goes through micrometres: the exact result is `VALUE * size(FROM) / size(TO)`. Round it to a whole number, rounding exact halves up (all values are non-negative). Use integer arithmetic only.

## Output

One line per non-blank input line, in input order:

- valid request: `VALUE FROM = RESULT TO` where VALUE is printed as the integer value (leading zeros removed) and RESULT is the rounded whole number.
- anything else (wrong number of words, bad VALUE, unknown unit): `line K: bad` where K is the line number.

No requests produce no output.

## Example

Input:

```
5 km mi
12 in cm

007 ft m
3 parsec m
2 mi
1 in um
```

Output:

```
5 km = 3 mi
12 in = 30 cm
7 ft = 2 m
line 5: bad
line 6: bad
1 in = 25400 um
```
