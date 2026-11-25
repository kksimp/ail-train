import re
import sys

lines = sys.stdin.read().splitlines()
toks = lines[0].split() if lines else []
ok = len(toks) == 6 and all(re.fullmatch(r"[0-9]+", t) for t in toks)
if ok:
    s, i, r, beta, gamma, days = (int(t) for t in toks)
    ok = beta <= 100 and gamma <= 100 and days <= 30 and s + i + r > 0
if not ok:
    print("invalid input")
else:
    n = s + i + r
    print(f"day 0: S={s} I={i} R={r}")
    peak, peak_day = i, 0
    end_day = 0 if i == 0 else None
    for d in range(1, days + 1):
        new_inf = s * i * beta // (n * 100)
        new_rec = i * gamma // 100
        s -= new_inf
        i += new_inf - new_rec
        r += new_rec
        print(f"day {d}: S={s} I={i} R={r}")
        if i > peak:
            peak, peak_day = i, d
        if i == 0 and end_day is None:
            end_day = d
    print(f"peak infected {peak} at day {peak_day}")
    if end_day is None:
        print("still active")
    else:
        print(f"ended on day {end_day}")
