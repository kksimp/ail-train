halve = lambda w: w // 2
cap = lambda w: min(w, 1024)
m8 = lambda w: w // 8 * 8
a64 = lambda w: max(w, 64)
thumb = [("halve", halve), ("halve", halve), ("multiple of 8", m8), ("at least 64", a64)]
preview = [("cap 1024", cap), ("multiple of 8", m8)]
def run(st, w):
    for _, f in st: w = f(w)
    return w
for label, st in [("thumb", thumb), ("preview", preview)]:
    print(f"{label}: {' > '.join(n for n, _ in st)}")
    print(f"  4000, 1366, 333, 150 -> {[run(st, w) for w in [4000, 1366, 333, 150]]}")
