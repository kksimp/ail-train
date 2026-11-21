I = {2015: 100.0, 2018: 105.9, 2020: 108.7, 2022: 121.7, 2024: 131.5, 2026: 136.8}
for n, y, o, t in [("bread", 2015, 1.10, 1.45), ("cinema", 2018, 8.50, 11.20), ("laptop", 2020, 899.0, 749.0), ("coffee", 2022, 2.80, 3.40), ("bus", 2024, 1.75, 1.75)]:
    r = o * I[2026] / I[y]; c = (t / r - 1.0) * 100.0; v = "dearer" if c > 0.5 else "cheaper" if c < -0.5 else "about the same"
    print(f"{n}: {o:.2f} in {y} = {r:.2f} today vs {t:.2f}, {v}")
