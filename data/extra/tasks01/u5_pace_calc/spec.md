# Running pace calculator

Reads runs from standard input, one per line: `METERS TIME`. METERS is 1 to 6 digits, at least 1. TIME is `MM:SS` (MM 1 or 2
digits, SS exactly 2 digits) or `H:MM:SS` (H 1 or 2 digits, MM and SS exactly 2 digits); MM and SS must be below 60, and the
total must be above zero. A blank line is skipped. Any other line is invalid and prints `line K: invalid`, K being its
1-based line number (blank lines count for numbering).

For a valid line print `METERSm TIME -> P/km S km/h` where
- P is the pace per kilometre as `M:SS`: total seconds x 1000 / METERS rounded to the nearest second, halves up
  (minutes may exceed 59, seconds are two digits);
- S is the speed in km/h with one decimal: meters x 36 / total seconds is the speed in tenths, rounded to the nearest tenth,
  halves up. Print it as `W.T` (whole part, one digit).
TIME is printed as written in the input.

After all lines, if any run was valid print `fastest: P/km (line K)` for the smallest unrounded pace (the lowest seconds per
kilometre; on equal pace the earliest line). If there was no valid run print `no runs` instead.

Example: `5000 25:00` gives `5000m 25:00 -> 5:00/km 12.0 km/h` and `fastest: 5:00/km (line 1)`.
