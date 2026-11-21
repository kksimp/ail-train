def pa(t):
    t = t.strip()
    if len(t) < 2: return None, f"'{t}' is too short"
    u = t[-1]; n = t[:-1]
    try: v = float(n)
    except ValueError: return None, f"'{n}' is not a number"
    c = v if u == "C" else (v - 32.0) * 5.0 / 9.0 if u == "F" else v - 273.15 if u == "K" else -1000.0
    if c == -1000.0: return None, f"unknown unit {u}"
    if c < -273.15: return None, f"{t} is below absolute zero"
    return c, None
G = []
for r in ["21.5C", "70F", "300K", "abcC", "12X", "-500F", "7", " 98.6F "]:
    c, e = pa(r)
    if e is None: G.append(c); print(f"{r.strip()} = {c:.2f} C")
    else: print(f"{r.strip()}: {e}")
print(f"{len(G)} good readings, mean {sum(G) / len(G):.2f} C")
