# Cricket batting averages

Reads innings from standard input, one per line: `PLAYER RUNS`. RUNS is 1 to 3 digits (0 allowed), optionally followed by `*`
meaning the batter was not out. Any other non-blank line is invalid (counted). Blank lines are skipped.

For each player (in no particular order until sorted) compute: INNS (innings count), NO (not-out count), RUNS (total),
HS (highest score, taken from the first innings that reached the maximum, written with `*` if that innings was not out),
the average, and the number of scores of 50 to 99 and of 100 or more.
The average is RUNS divided by the number of dismissals (INNS - NO), rounded to the nearest hundredth with halves up, and
printed with two decimals; with no dismissals it is `-`.

Print one line per player: `NAME inns=I no=N runs=R hs=H avg=A 50=F 100=C`, sorted by average descending (a player with
no dismissals counts as the highest average), then total RUNS descending, then NAME (byte order).
Then `invalid: K` if K > 0. If there is no valid innings print `no innings` (before the `invalid` line, if any).

Example: `amy 40`, `amy 61*`, `amy 10` gives `amy inns=3 no=1 runs=111 hs=61* avg=55.50 50=1 100=0`.
