E = {"food": 40000, "transport": 12000, "fun": 8000, "buffer": 10000}
for n, c in [("food", 12500), ("fun", 4500), ("transport", 6000), ("fun", 5200), ("food", 30100), ("transport", 7000)]:
    if E[n] >= c: E[n] -= c; print(f"{n} -{c}: ok, {E[n]} left")
    else: s = c - E[n]; E[n] = 0; E["buffer"] -= s; print(f"{n} -{c}: short {s}, buffer now {E['buffer']}")
for n in ["food", "transport", "fun", "buffer"]: print(f"{n}: {E[n] // 100}.{E[n] % 100:02}")
