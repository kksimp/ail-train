C = {1: 820, 2: 1050, 3: 1320}
for n, T in [("Mon", [(1, 290), (1, 290), (1, 290), (1, 290)]), ("Tue", [(2, 350), (1, 290), (2, 350), (2, 350)]), ("Wed", [(1, 190)]), ("Thu", [(3, 480), (3, 480), (1, 290), (2, 350)])]:
    tp = max(t[0] for t in T); cp = C[tp]; sp = 0; ch = []
    for z, f in T:
        if sp + f > cp: f = cp - sp
        sp += f; ch.append(str(f))
    print(f"{n} (zones 1-{tp}, cap {cp}): {' + '.join(ch)} = {sp}")
