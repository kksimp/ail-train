# units

Normalize unit-annotated quantities from standard input to base units.

Input: one quantity per line, such as `5 km` or `250g`: 1 to 12 digits (no sign, no decimal point), optional spaces, then a unit made of letters. Empty lines are ignored; surrounding spaces on a line are ignored. Known units (case-sensitive):
- length, base `m`: `mm`, `cm`, `m`, `km` (1 cm = 10 mm, 1 m = 1000 mm, 1 km = 1000 m)
- mass, base `g`: `mg`, `g`, `kg` (1 g = 1000 mg, 1 kg = 1000 g)
- time, base `s`: `ms`, `s`, `min`, `h` (1 s = 1000 ms, 1 min = 60 s, 1 h = 60 min)

For each line print `TEXT = VALUE BASE`, where TEXT is the trimmed line as written and VALUE is the quantity in the base unit written as a decimal number with no trailing zeros (and no `.` when it is whole), exactly, with at most 3 decimals: `5 cm = 0.05 m`. A line that does not match (bad number, unknown unit, too many digits) prints `TEXT = invalid`.

After the lines, print a total for each category that had at least one valid line, in the order length, mass, time: `total length: VALUE m`, `total mass: VALUE g`, `total time: VALUE s`. Totals use the same number format.

Example input:
```
5 km
250 cm
1500mg
90 min
12 parsecs
```
Example output:
```
5 km = 5000 m
250 cm = 2.5 m
1500mg = 1.5 g
90 min = 5400 s
12 parsecs = invalid
total length: 5002.5 m
total mass: 1.5 g
total time: 5400 s
```
