def hy(k, a): return 0 if a == 0 else 15 if a == 1 else 24 if a == 2 else 24 + (a - 2) * (5 if k == "dog" else 4)
T = sorted([(n, k, a, hy(k, a)) for n, k, a in [("Rex", "dog", 7), ("Mog", "cat", 12), ("Bea", "dog", 2), ("Tib", "cat", 4), ("Odie", "dog", 11), ("Zaz", "cat", 1)]], key=lambda p: (-p[3], p[0]))
for p in T: print(f"{p[0]:<5} {p[1]:<4} {p[2]:>2} -> {p[3]:>3}")
print(f"oldest in human years: {T[0][0]}")
