O = [("Ash", ["robin", "wren", "robin", "blackbird", "jay"]), ("Bay", ["robin", "jay", "heron", "wren", "wren"]), ("Cam", ["robin", "wren", "kite", "jay", "robin", "robin"])]; c = {}; sb = {}
for w, bs in O:
    for b in bs: c[b] = c.get(b, 0) + 1; sb.setdefault(b, set()).add(w)
S = sorted(c)
print("seen by all: " + ", ".join(s for s in S if len(sb[s]) == 3)); print("seen by one: " + ", ".join(s for s in S if len(sb[s]) == 1))
for s in sorted(S, key=lambda s: (-c[s], s))[:3]: print(f"{s}: {c[s]}")
