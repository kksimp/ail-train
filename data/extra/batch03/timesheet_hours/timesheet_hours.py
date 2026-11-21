def mins(t):
    p = t.split(":")
    if len(p) != 2: return None
    try: h, m = int(p[0]), int(p[1])
    except ValueError: return None
    if not (0 <= h <= 23 and 0 <= m <= 59): return None
    return h * 60 + m
hm = lambda x: f"{x // 60}:{x % 60:02d}"
w = 0
for s, e in [("08:00", "16:30"), ("07:45", "17:15"), ("09:00", "18:00"), ("8:30", "17:00"), ("10:00", "25:00"), ("06:15", "15:45")]:
    a, b = mins(s), mins(e)
    if a is None or b is None: print(f"{s}-{e}: bad time"); continue
    w += b - a; print(f"{s}-{e}: {hm(b - a)}")
r = min(w, 2400)
print(f"total {hm(w)}, regular {hm(r)}, overtime {hm(w - r)}")
