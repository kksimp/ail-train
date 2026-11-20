bal, lim = 100, 50
for kind, amt in [("in", 40), ("out", 120), ("out", 80), ("out", 60), ("in", 25), ("out", 10)]:
    if kind == "in":
        bal += amt
        print(f"deposit {amt}: balance {bal}")
    else:
        ok = bal - amt >= -lim
        if ok: bal -= amt
        print(f"withdraw {amt}: {'ok' if ok else 'refused'}, balance {bal}")
print(f"Noor ends at {bal}, headroom {bal + lim}")
