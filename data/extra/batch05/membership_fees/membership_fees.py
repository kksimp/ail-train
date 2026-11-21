def fe(a): return 0 if a < 5 else 4000 if a < 18 else 5000 if a >= 65 else 9000
for n, A in [("Ito", [41, 39, 12, 9, 3]), ("Lund", [70, 68]), ("Moss", [35, 16, 14, 11]), ("Nair", [29])]:
    f = sum(fe(a) for a in A); b = min(f, 20000); print(f"{n}: {len(A)} members, {f // 100} before cap, pays {b // 100}, saves {(f - b) // 100}")
