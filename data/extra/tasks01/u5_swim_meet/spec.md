# Swim meet results with ties

Reads race results from standard input, one per line: `EVENT SWIMMER TEAM TIME` (four words). TIME is `SS.hh` or
`M:SS.hh`: seconds with exactly two digits of hundredths; SS is 1 or 2 digits (below 60); with minutes, M is 1 or 2 digits
and SS is exactly 2 digits. The time must be above zero. A blank line is ignored. Any other line that is not valid, or that
repeats a SWIMMER already in the same EVENT, is malformed: skipped and counted.

Events are reported in order of first appearance, each as `== EVENT ==` followed by one line per swimmer, fastest first
(ties broken by SWIMMER name, byte order): `RANK SWIMMER TEAM TIME pts=P`, TIME as written in the input.
RANK is a competition rank: swimmers with equal times share a rank, and the next rank skips accordingly (1, 2, 2, 4).
Points for places 1 to 8 are 9, 7, 6, 5, 4, 3, 2, 1 and nothing below. Swimmers tied over places p..q split the points of
those places evenly: each gets (sum of the points of those places) / (number tied), integer division rounding down.

After all events print `== teams ==` and one line per team `TEAM POINTS` (all teams that appear), by points descending then
name. Finally `malformed: K` only if K > 0. With no valid result at all print `no results` first (then any malformed line).

Example: `50free amy RED 27.10`, `50free bo BLU 27.10`, `50free cy RED 28.00` gives
```
== 50free ==
1 amy RED 27.10 pts=8
1 bo BLU 27.10 pts=8
3 cy RED 28.00 pts=6
== teams ==
RED 14
BLU 8
```
