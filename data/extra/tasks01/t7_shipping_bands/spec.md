Read parcels from standard input, one per line: `id,grams,zone`. Blank lines are ignored. Fields are trimmed; the id must be
non-empty; grams is an integer >= 1; zone is 1, 2 or 3; exactly 3 fields. Any other line prints `line N: invalid`
(N is the 1-based line number, blank lines counted). A parcel over 50000 grams prints `line N: too heavy` instead.

Weight bands and base prices in cents: S (up to 500 g) 500; M (up to 2000 g) 900; L (up to 5000 g) 1500;
X (up to 20000 g) 3000; H (over 20000 g) 3000 plus 200 for each started 1000 g above 20000 g.
The zone multiplier in percent is 100 for zone 1, 125 for zone 2, 160 for zone 3. The cost is
(base * percent + 50) / 100 with integer division (rounded half up).

For each valid parcel print `ID: band=B zone=Z cost=C` (money in dollars with two decimals). After the input print, for
each band in the order S, M, L, X, H that has at least one parcel, `band B: K parcels, T` with the count and cost sum, then
`total: T`.

Example input:
    a1,450,1
    b2,21500,2
Output:
    a1: band=S zone=1 cost=5.00
    b2: band=H zone=2 cost=44.75
    band S: 1 parcels, 5.00
    band H: 1 parcels, 44.75
    total: 49.75

With no valid parcels print only `total: 0.00`.
