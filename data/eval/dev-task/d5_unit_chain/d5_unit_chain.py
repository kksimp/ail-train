import sys

F = {"um": 1, "mm": 1000, "cm": 10000, "m": 1000000, "km": 1000000000,
     "in": 25400, "ft": 304800, "yd": 914400, "mi": 1609344000}

for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    if (len(w) != 3 or not (w[0].isascii() and w[0].isdigit()) or len(w[0]) > 9
            or w[1] not in F or w[2] not in F):
        print(f"line {k}: bad")
        continue
    n = int(w[0])
    # round half up of n * F[from] / F[to]
    r = (n * F[w[1]] * 2 + F[w[2]]) // (2 * F[w[2]])
    print(f"{n} {w[1]} = {r} {w[2]}")
