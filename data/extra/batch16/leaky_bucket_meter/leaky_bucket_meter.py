arrivals = [0, 1, 2, 3, 4, 5, 12, 13, 30, 31, 32, 33, 34, 35]
rate = 4
cap = 3
leaves = []
last = -rate
dropped = 0
for t in arrivals:
    waiting = sum(1 for d in leaves if d > t)
    if waiting >= cap:
        dropped += 1
        print(f"t={t:>2}: dropped, {waiting} already waiting")
        continue
    out = max(last + rate, t)
    leaves.append(out)
    last = out
    print(f"t={t:>2}: queued, leaves at {out:>2} (waited {out - t})")
gaps = [leaves[i] - leaves[i - 1] for i in range(1, len(leaves))]
print(f"departure gaps {gaps}")
print(f"sent {len(leaves)}, dropped {dropped}")
