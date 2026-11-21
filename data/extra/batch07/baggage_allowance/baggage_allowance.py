I = {"basic": 0, "standard": 1, "flex": 2}
for n, f, C, H in [("Ito", "basic", [6.5], [19.0]), ("Kerr", "standard", [7.8], [22.0]), ("Lam", "flex", [5.0], [24.5, 18.0]), ("Moya", "standard", [6.9], [21.0, 15.0]), ("Ng", "flex", [4.0], [23.0, 23.1, 10.0])]:
    fe = 0; N = []
    for c in C:
        if c > 7.0: fe += 40; N.append(f"cabin bag {c:.1f} kg to hold")
    for i, h in enumerate(H):
        if i >= I[f]: fe += 50; N.append("extra bag")
        if h > 23.0: fe += 75; N.append(f"{h:.1f} kg overweight")
    print(f"{n} ({f}): {', '.join(N) if N else 'all fine'}, fees {fe}")
