import math
def ph(c): return 0.0 - math.log10(c)
def kind(p): return "acidic" if p < 6.9 else "basic" if p > 7.1 else "neutral"
for n, c in [("stomach acid", 0.01), ("lemon juice", 0.005), ("coffee", 0.00001), ("pure water", 0.0000001), ("sea water", 0.00000001), ("soap", 0.0000000001)]:
    p = ph(c); print(f"{n:<12} pH {p:>5.2f}, pOH {14.0 - p:>5.2f} ({kind(p)})")
c = 0.1; st = []
for k in range(5): st.append(f"{ph(c):.1f}"); c = c / 10.0
print(f"diluting 0.1 M acid tenfold: {' -> '.join(st)}")
