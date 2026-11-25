# Chess Elo updates with integer rounding

Reads games from standard input, one per line: `A B R` (three words). A and B are different player names; R is `W` (A won),
`L` (B won) or `D` (draw). A blank line is skipped. Any other line prints `line K: invalid` (K = 1-based physical line number).

Every player starts at rating 1500 with 0 games. For a valid game, using the ratings before it:
- d = ratingA - ratingB. hi = 50 + min(|d|, 400) / 10 (integer division). The expected score of A, in percent, is hi if
  d >= 0, otherwise 100 - hi. B's expected percent is 100 minus that.
- Actual score in percent: 100 win, 50 draw, 0 loss (B gets 100 minus A's).
- K is 32 for a player with fewer than 10 games before this game, otherwise 16 (each player separately).
- change = K * (actual - expected) / 100, rounded to the nearest integer with halves away from zero (so 2.5 becomes 3 and
  -2.5 becomes -3). The new rating is the old one plus the change, but never below 100.
- Both games counts go up by one.

Print for each valid game `A OLD->NEW B OLD->NEW` using the ratings before and after. After the last line, print one line per
player sorted by rating descending then name (byte order): `NAME RATING GAMES`. If no game was valid print `no games` at the end.

Example: `amy bo W` prints `amy 1500->1516 bo 1500->1484`.
