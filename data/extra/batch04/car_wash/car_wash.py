T = {"basic": 6, "deluxe": 11, "full": 18}
cl = idle = worst = 0
for a, k in [(0, "basic"), (2, "full"), (5, "basic"), (9, "deluxe"), (100, "basic"), (101, "full"), (103, "deluxe"), (110, "polish")]:
    if a > cl: idle += a - cl; cl = a
    w = cl - a; worst = max(worst, w); f = cl + T.get(k, 8)
    print(f"{k:<7} arrives {a:>2}, starts {cl:>2}, done {f:>2}, waited {w}"); cl = f
print(f"bay idle {idle} min, longest wait {worst} min, last car done at {cl}")
