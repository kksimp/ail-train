def mv(n, f, t, s, out):
    if n == 0: return
    mv(n - 1, f, s, t, out); out.append(f"disc {n}: {f} -> {t}"); mv(n - 1, s, t, f, out)
o = []; mv(3, "A", "C", "B", o)
for m in o: print(m)
for n in [1, 5, 10, 16]:
    o = []; mv(n, "A", "C", "B", o); print(f"{n} discs: {len(o)} moves, formula {2 ** n - 1}")
