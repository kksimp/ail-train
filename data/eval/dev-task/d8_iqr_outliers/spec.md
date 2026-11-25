# iqr_outliers

Reads a series of non-negative integers and reports its quartiles and the values outside the interquartile-range fences.

## Input

Zero or more lines, each holding values separated by spaces. Together the values of all lines form the series, in input order. A value is a non-empty run of ASCII digits.

## Rules

1. If any value is not a run of digits, print `bad value: TOKEN` (TOKEN being the first such value in input order) and stop.
2. If the series has fewer than 4 values, print `need at least 4 values` and stop.
3. Sort the values ascending. The median of a sorted list is its middle value if the count is odd, else the mean of its two middle values (so it may end in .5).
4. Q1 is the median of the lower half and Q3 is the median of the upper half. For a count N, the lower half is the first N/2 sorted values (integer division) and the upper half is the last N/2 sorted values; when N is odd, the middle value is in neither half.
5. IQR = Q3 - Q1. The lower fence is Q1 - 1.5 * IQR and the upper fence is Q3 + 1.5 * IQR.
6. A value is an outlier if it is strictly below the lower fence or strictly above the upper fence.

All of Q1, Q3, IQR and the fences are exact multiples of 0.25. Print each as a decimal with exactly two digits after the point (`3.50`, `12.00`); a negative number has a leading `-` (`-4.25`).

## Output

```
n: N
q1: Q1
q3: Q3
iqr: IQR
fences: LOWER UPPER
```

then, in input order, one line `outlier: P V` for every outlier, P being its 1-based position in the input series and V its value; or the single line `outliers: none` if there is none.

## Example

Input:

```
7 9 10 12 13
14 15 40 11
```

Output:

```
n: 9
q1: 9.50
q3: 14.50
iqr: 5.00
fences: 2.00 22.00
outlier: 8 40
```
