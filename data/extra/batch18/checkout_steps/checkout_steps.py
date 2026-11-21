shelf = {"lamp": 5, "rug": 1}
orders = [(1, "lamp", 2, True, "AB1 2CD"), (2, "rug", 2, True, "EF3 4GH"), (3, "lamp", 1, False, "IJ5 6KL"), (4, "lamp", 3, True, "ZZ9 9ZZ")]
for i, it, q, ok, pc in orders:
    have = shelf.get(it, 0)
    if have < q: print(f"order {i} stopped: only {have} {it} on the shelf"); continue
    if not ok: print(f"order {i} stopped: card declined for {q * 1250} cents"); continue
    if pc.startswith("ZZ"): print(f"order {i} stopped: no courier to {pc}"); continue
    print(f"order {i}: {q * 1250} cents, label CR-{len(pc) * 7}, {have - q} {it} left")
