def mn(t): h, m = t.split(":"); return int(h) * 60 + int(m)
d = 0; sh = ("", 10000); la = ("", -1)
for dy, b, w in [("Mon", "23:10", "06:45"), ("Tue", "22:40", "06:50"), ("Wed", "00:30", "07:00"), ("Thu", "23:55", "06:30"), ("Fri", "01:15", "09:20"), ("Sat", "23:30", "08:10"), ("Sun", "22:20", "06:40")]:
    bb = mn(b); bs = bb + 1440 if bb < 720 else bb; s = mn(w) - bb
    if s < 0: s += 1440
    d += 480 - s
    if s < sh[1]: sh = (dy, s)
    if bs > la[1]: la = (dy, bs)
    print(f"{dy}: {s // 60}h{s % 60:02}, debt {d} min")
print(f"shortest night {sh[0]}; latest to bed {la[0]}")
