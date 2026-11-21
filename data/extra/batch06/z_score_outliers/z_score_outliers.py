for nm, X in [("north", [20.1, 20.4, 19.8, 20.0, 27.9, 20.2, 19.9, 20.3]), ("south", [15.2, 15.0, 15.4, 14.9, 15.1, 15.3, 15.0, 15.2]), ("roof", [8.0, 9.5, 7.2, 8.8, 1.1, 8.4, 9.0, 8.1])]:
    n = float(len(X)); m = sum(X) / n; ss = 0.0
    for x in X: ss += (x - m) * (x - m)
    sd = (ss / n) ** 0.5; F = []
    for i, x in enumerate(X):
        z = (x - m) / sd
        if abs(z) > 2.0: F.append(f"#{i + 1} {x:.1f} (z {z:.2f})")
    print(f"{nm}: mean {m:.3f}, sd {sd:.3f}, outliers {', '.join(F) if F else 'none'}")
