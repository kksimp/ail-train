class Gcra:
    def __init__(s, interval, tolerance):
        s.interval, s.tolerance, s.tat = interval, tolerance, 0
    def check(s, t):
        allowed_at = s.tat - s.tolerance
        if t < allowed_at:
            return allowed_at - t
        s.tat = max(s.tat, t) + s.interval
        return 0

g = Gcra(10, 25)
times = [0, 1, 2, 3, 4, 20, 25, 40, 41, 42, 90, 91, 92, 93, 94]
ok = 0
for t in times:
    wait = g.check(t)
    if wait == 0:
        ok += 1
        print(f"t={t:>3} allowed, next theoretical arrival {g.tat}")
    else:
        print(f"t={t:>3} limited, retry in {wait}")
print(f"allowed {ok} of {len(times)}")
