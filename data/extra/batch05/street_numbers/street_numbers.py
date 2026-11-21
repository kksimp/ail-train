def inf(n, l):
    s = "odd" if n % 2 else "even"; nb = [str(x) for x in (n - 2, n + 2) if 1 <= x <= l]; o = n + 1 if n % 2 else n - 1
    return f"{s} side, next to {' and '.join(nb)}, opposite {o if 1 <= o <= l else 'none'}"
for n in [1, 2, 7, 12, 23, 24]: print(f"{n}: {inf(n, 24)}")
