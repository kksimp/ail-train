def mn(t): h, m = t.split(":"); return int(h) * 60 + int(m)
p = 0
for d, a, b in [("Mon", "08:00", "16:30"), ("Tue", "07:45", "18:15"), ("Wed", "09:00", "17:00"), ("Thu", "08:30", "19:00"), ("Sat", "10:00", "14:30")]:
    w = mn(b) - mn(a)
    if d in ("Sat", "Sun"): c = w * 1450 * 2 // 60
    else: n = min(w, 480); c = n * 1450 // 60 + (w - n) * 1450 * 3 // 120
    p += c; print(f"{d}: {w // 60}h{w % 60:02} -> {c // 100}.{c % 100:02}")
print(f"week: {p // 100}.{p % 100:02}")
