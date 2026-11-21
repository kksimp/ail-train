def place(n, st, ln, ac):
    r, c = ord(st[0]) - 65, int(st[1:]) - 1
    return (n, [(r, c + i) if ac else (r + i, c) for i in range(ln)])
fleet = [place("carrier", "A1", 4, True), place("sub", "C3", 3, False), place("boat", "F6", 2, True)]
hits = set()
for call in ["A1", "B2", "C3", "A2", "D3", "E3", "A3", "A4", "F7", "F6", "J9"]:
    t = (ord(call[0]) - 65, int(call[1:]) - 1)
    s = next((s for s in fleet if t in s[1]), None)
    if s:
        hits.add(t)
        print(f"{call}: " + (f"sunk {s[0]}" if all(c in hits for c in s[1]) else "hit"))
    else:
        print(f"{call}: miss")
print("still afloat: " + ", ".join(s[0] for s in fleet if not all(c in hits for c in s[1])))
