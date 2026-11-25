# Tournament bracket progression

Simulates a single-elimination bracket from a list of results.

Line 1: the players in seed order, separated by commas (names have no commas; trim spaces around each). If there are fewer
than 2 players print `error: need 2 players` and stop. If a name repeats print `error: duplicate player NAME` (first
repeated name) and stop.

Round 1 pairs players in order: 1st vs 2nd, 3rd vs 4th, and so on. If a round has an odd number of players, the last one
gets a bye and goes through automatically (a bye is listed last in the round).
Every later line is a result `WINNER LOSER` (two words). It applies only if the two names are an undecided match of the
current round (in either order); it decides that match. Anything else (blank lines are skipped, not counted) is ignored and
counted. When all matches of the current round are decided, the next round is formed from the winners in the same order
(bye players keep their place), until one player remains: the champion. Results after that are ignored.

Output: for each round started, `Round N:` then one line per match: `  A vs B -> WINNER` or `  A vs B -> pending`,
and `  A bye` for a bye. Then `Champion: NAME` or `Champion: none yet`. Then `ignored results: K` only if K > 0.

Example: line 1 `a,b,c`, then `b a` and `c b` gives
```
Round 1:
  a vs b -> b
  c bye
Round 2:
  b vs c -> c
Champion: c
```
