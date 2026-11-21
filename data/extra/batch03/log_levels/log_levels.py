L = ["INFO started", "DEBUG cache warm", "WARN disk 85%", "INFO request /a", "ERROR timeout on db", "TRACE noisy", "WARN retrying", "ERROR gave up"]
N = ["DEBUG", "INFO", "WARN", "ERROR"]
c = [0] * 4; fe = -1
for i, l in enumerate(L):
    w = l.split(" ")[0]
    if w not in N: print(f"line {i + 1}: unknown level {w}"); continue
    c[N.index(w)] += 1
    if w == "ERROR" and fe < 0: fe = i + 1
print(" ".join(f"{n}={c[i]}" for i, n in enumerate(N)))
for l in L:
    w = l.split(" ")[0]
    if (N.index(w) if w in N else 0) >= 2: print(f"  {l}")
print(f"first error on line {fe}")
