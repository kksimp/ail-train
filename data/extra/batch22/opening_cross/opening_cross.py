buys = [(102, 300), (101, 200), (100, 400), (99, 300), (98, 500)]
sells = [(97, 200), (98, 300), (99, 300), (100, 300), (101, 400), (103, 500)]
best = 0
best_vol = -1
best_gap = 0
for p in range(97, 104):
    b = sum(q for l, q in buys if l >= p)
    s = sum(q for l, q in sells if l <= p)
    vol = min(b, s)
    gap = abs(b - s)
    print(f"{p}: buyers {b:>4}, sellers {s:>4}, trades {vol:>4}, imbalance {gap:>4}")
    if vol > best_vol or (vol == best_vol and gap < best_gap):
        best, best_vol, best_gap = p, vol, gap
print(f"opening price {best}: {best_vol} shares trade, {best_gap} left unmatched")
