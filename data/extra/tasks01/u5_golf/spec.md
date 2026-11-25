# Golf scorecards vs par

Line 1 gives the par of each hole: 1 to 36 integers between 3 and 6 separated by spaces. If it is not valid print
`error: bad pars` and stop.

Each later non-blank line is a scorecard: `NAME s1 s2 ... sN` with exactly one score per hole. A score is a stroke count (1 to
2 digits, at least 1) or `-` for a hole not finished, which counts as par + 3. A card with the wrong number of scores, a bad
score, or a NAME already seen on an earlier card is skipped and counted.

For each player compute TOTAL strokes and TOPAR = TOTAL minus total par, and the number of holes that were: eagle or better
(2 or more under par), birdie (1 under), par, bogey (1 over), double bogey or worse (2 or more over).
Print players by TOPAR ascending, then NAME (byte order): `RANK NAME TOTAL TOPAR E/B/P/Bo/D`. RANK is a competition rank
(equal TOPAR share it and the next skips, as 1, 2, 2, 4) written `T` + number when shared, e.g. `T2`.
TOPAR is printed as `E` for 0, `+N` above, `-N` below. The five counts are joined with `/` in the order above.

Finally `skipped: K` if K > 0. With no valid card print `no scorecards` (before any `skipped` line).

Example: pars `4 3 5`, card `amy 4 2 7` gives `1 amy 13 E 0/1/1/0/1`.
