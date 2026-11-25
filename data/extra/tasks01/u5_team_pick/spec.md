# Team selection by ratings

Splits players into two balanced teams, A and B. Each non-blank input line is `NAME RATING`: RATING is an integer from 1 to
100 (1 to 3 digits, no sign). Any other line, or a NAME already seen, is invalid: skipped and counted.

Players are taken in order of RATING descending, then NAME (byte order). With n valid players each team holds at most
(n + 1) / 2 players (integer division). The next player goes to
1. the other team if one team is already full;
2. otherwise the team with the lower rating sum;
3. on equal sums, the team with fewer players;
4. otherwise team A.

Print `Team A: NAMES (total S)` and `Team B: NAMES (total S)`, NAMES being the members in the order picked, separated by
single spaces, then `difference: D` (the absolute difference of the sums). Then `invalid: K` if K > 0.
With fewer than 2 valid players print `need at least 2 players` instead of the three lines (the `invalid` line may follow).

Example: amy 90, bo 80, cy 70, di 60 gives
```
Team A: amy di (total 150)
Team B: bo cy (total 150)
difference: 0
```
