# Length total

Read lines of lengths from standard input and print their total in metres.

## Input
Lines are numbered from 1. Each line is split into words on runs of whitespace (spaces or tabs); a line with no words is skipped (it still counts for numbering).
A line is valid when it has exactly two words, the first consisting only of the digits `0-9` (leading zeros allowed; no sign, no decimal point) and the second being one of the units `mm`, `cm`, `m`, `km` (case-sensitive).
Unit sizes in millimetres: `mm` = 1, `cm` = 10, `m` = 1000, `km` = 1000000.

## Rules
Every invalid line prints `error: line N` (N is its line number) immediately and is otherwise ignored.
The total, in millimetres, is the sum of value times unit size over the valid lines. All values fit in 64-bit signed integers.

## Output
After all lines, print `total: M.FFF m` where `M` is the total in whole metres (total millimetres divided by 1000, rounded down) and `FFF` is the remaining millimetres (total modulo 1000) written with exactly three digits, zero padded. Error lines come first, in input order. With no valid lines the total line is `total: 0.000 m`.

## Example
Input:
```
3 km
250 m
40 cm
7 mm
```
Output:
```
total: 3250.407 m
```
