checks = [["battery", 87, 30, 100], ["gps sats", 9, 6, 99], ["wind", 38, 0, 35], ["motor temp", 41, 0, 70], ["prop hours", 147, 0, 150], ["signal", 72, 50, 100]]
ok = lambda c: c[2] <= c[1] <= c[3]
near = lambda c: ok(c) and (c[1] - c[2] < 5 or c[3] - c[1] < 5)
def verdict(label, cs):
    print(f"{label}: ready {'true' if all(ok(c) for c in cs) else 'false'}")
    bad = next((c for c in cs if not ok(c)), None)
    if bad: print(f"  first failure: {bad[0]} {bad[1]} (allowed {bad[2]}-{bad[3]})")
    w = [c[0] for c in cs if near(c)]
    if w: print(f"  near a limit: {', '.join(w)}")
verdict("09:00", checks)
later = [list(c) for c in checks]
for c in later:
    if c[0] == "wind": c[1] = 22
verdict("11:00", later)
print(f"09:00 wind still {checks[2][1]}")
