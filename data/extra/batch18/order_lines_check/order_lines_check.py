prices = {"MUG-01": 850, "TEA-50": 499, "POT-02": 2450}
def cost(l):
    p = l.split(" x ")
    if len(p) != 2: return None, f"cannot read '{l}'"
    q = p[0].strip()
    if not q.lstrip("-").isdigit(): return None, f"bad quantity in '{l}'"
    q = int(q); s = p[1].strip()
    if s not in prices: return None, f"no such product {s}"
    if q <= 0: return None, f"quantity must be positive in '{l}'"
    return q * prices[s], None
good = 0
for i, o in enumerate([["2 x MUG-01", "1 x TEA-50"], ["1 x POT-02", "3 x CUP-09"], ["two x TEA-50"], ["4 x TEA-50", "1 x POT-02", "1 x MUG-01"], ["1 x MUG-01", "0 x TEA-50"]]):
    t = 0; err = None
    for l in o:
        c, err = cost(l)
        if err: break
        t += c
    if err: print(f"order {i + 1}: rejected, {err}"); continue
    good += t; print(f"order {i + 1}: {t // 100}.{t % 100:02}")
print(f"accepted value {good // 100}.{good % 100:02}")
