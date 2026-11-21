from itertools import combinations
from math import comb
sq = ["Ash", "Bea", "Cal", "Dev", "Eli", "Fay"]
sk = {"Ash": 7, "Bea": 9, "Cal": 4, "Dev": 6, "Eli": 8, "Fay": 5}
for k in [2, 3]: print(f"choose {k} of {len(sq)}: {len(list(combinations(sq, k)))} ways (Pascal says {comb(len(sq), k)})")
for t in combinations(sq, 3):
    if sum(sk[n] for n in t) == 20: print(f"  total 20: {', '.join(t)}")
