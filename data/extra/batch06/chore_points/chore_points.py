V = {"bed": 1, "dishes": 3, "bins": 2, "hoover": 4, "laundry": 3, "garden": 5}
for w, d in [("Mia", ["bed", "bed", "dishes", "bins", "hoover", "laundry", "bed"]), ("Neo", ["garden", "garden", "hoover", "dishes"]), ("Ola", ["bed", "dishes", "bins", "hoover", "garden", "laundry", "garden", "garden"])]:
    p = sum(V[c] for c in d); b = 5 if len(set(d)) >= 5 else 0; t = p + b; c = min(500, t * 10); print(f"{w}: {p} + {b} bonus = {t} points, {c // 100}.{c % 100:02}")
