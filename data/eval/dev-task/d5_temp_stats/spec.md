# d5_temp_stats

Write a command-line program that reads a temperature log from standard input and prints summary statistics.

## Input

Zero or more lines. Each line is one reading in integer tenths of a degree Celsius: after removing leading and trailing whitespace, a valid reading is an optional `-` followed by one or more ASCII digits (leading zeros are allowed, so `007` is 7; `+5`, `5.0`, `1e3` and `abc` are not valid). Blank lines (empty or only whitespace) are ignored and not counted at all. Any other non-blank line is invalid and is only counted as skipped. All valid readings fit comfortably in 32 bits.

## Rules

Let the valid readings be v1..vn, n being how many there are.

- `range` is printed as the smallest reading followed by the largest reading.
- `mean` is the sum divided by n, rounded to the nearest tenth with exact halves rounded away from zero (so a sum of 5 over n=2 gives 3 tenths, and a sum of -5 over n=2 gives -3 tenths). Use integer arithmetic only.
- `above` is how many readings are strictly greater than that rounded mean.

A value v in tenths is printed as degrees with exactly one decimal: a `-` if v is negative, then the absolute value divided by 10 (no leading zeros besides a single `0`), a `.`, and the last digit. For example 215 prints `21.5`, -5 prints `-0.5`, 0 prints `0.0`.

## Output

Always print these two lines first:

```
count N
skipped S
```

N is the number of valid readings and S the number of invalid non-blank lines. If N is 0, stop there. Otherwise print three more lines, in this order and with these exact words:

```
range LOW HIGH
mean X
above K
```

## Example

Input:

```
215
-30
abc

187
+4
-5
  120
```

Output:

```
count 5
skipped 2
range -3.0 21.5
mean 9.7
above 3
```
