def pay(a, notes, stock, i):
    if a == 0: return [0] * len(notes)
    if i >= len(notes): return None
    for k in range(min(a // notes[i], stock[i]), -1, -1):
        r = pay(a - k * notes[i], notes, stock, i + 1)
        if r is not None:
            r = list(r); r[i] = k; return r
    return None
notes = [100, 50, 20, 10]; stock = [2, 1, 4, 3]
for a in [180, 260, 70, 30, 500, 15]:
    u = pay(a, notes, stock, 0)
    if u is not None:
        parts = [f"{notes[i]}x{u[i]}" for i in range(len(notes)) if u[i] > 0]
        for i in range(len(notes)): stock[i] -= u[i]
        print(f"{a}: {' '.join(parts)}  stock now {'/'.join(map(str, stock))}")
    else:
        print(f"{a}: cannot pay")
