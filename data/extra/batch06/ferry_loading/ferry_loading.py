Q = [("car", 4), ("van", 6), ("lorry", 16), ("car", 4), ("bus", 12), ("car", 5), ("lorry", 15), ("car", 4), ("caravan", 11), ("car", 4)]; R = [40, 40]; L = [[], []]; W = []
for i, (k, n) in enumerate(Q):
    l = 0 if R[0] >= R[1] else 1; lb = f"{k}{i + 1}"
    if n <= R[l]: R[l] -= n; L[l].append(lb)
    else: W.append(lb)
for l in range(2): print(f"lane {l + 1} ({40 - R[l]} m): {' '.join(L[l])}")
print(f"waiting: {' '.join(W)}")
