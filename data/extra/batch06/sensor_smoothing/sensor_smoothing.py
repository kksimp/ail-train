R = [20.1, 20.4, 20.2, 26.0, 20.6, 20.9, 21.1, 14.2, 21.4, 21.7, 21.6, 22.0]; e = R[0]; S = []
for i, r in enumerate(R):
    if i > 0:
        if abs(r - e) > 3.0: S.append(i); print(f"{i:>2}: {r:.1f} spike (ema {e:.2f})"); continue
        e = 0.3 * r + (1.0 - 0.3) * e
    print(f"{i:>2}: {r:.1f} ema {e:.2f}")
print(f"spikes at {', '.join(map(str, S))}")
