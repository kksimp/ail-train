q = [("Asha", 160), ("Ben", 175), ("Chen", 168), ("Dora", 181), ("Eko", 150), ("Fia", 150)]
for i, (n, h) in enumerate(q):
    t = next((m for m, hh in q[i + 1:] if hh > h), "-")
    print(f"{n:<5} -> {t}")
