M = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]
for num in ["0123", "4567", "89", "2026"]:
    T = []; Mi = []; Bo = []; lit = 0
    for c in num:
        m = M[int(c)]; s = lambda b, ch: ch if m & b else " "
        T.append(f" {s(1, '_')} "); Mi.append(s(32, "|") + s(64, "_") + s(2, "|")); Bo.append(s(16, "|") + s(8, "_") + s(4, "|")); lit += bin(m).count("1")
    print(" ".join(T).rstrip()); print(" ".join(Mi).rstrip()); print(" ".join(Bo).rstrip()); print(f"{num}: {lit} segments lit")
