def bub(xs):
    xs = list(xs); sw = ps = 0; done = False
    while not done:
        done = True; ps += 1
        for i in range(1, len(xs) - ps + 1):
            if xs[i - 1] > xs[i]: xs[i - 1], xs[i] = xs[i], xs[i - 1]; sw += 1; done = False
        print(f"  pass {ps}: {xs}")
    return xs, sw, ps
for s in [[1, 2, 4, 3, 5, 6], [5, 4, 3, 2, 1]]:
    print(f"start {s}")
    _, sw, ps = bub(s)
    print(f"{sw} swaps in {ps} passes")
