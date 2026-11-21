P = [("Ana", [(540, 600), (720, 780), (900, 990)]), ("Ben", [(570, 660), (750, 840), (960, 1020)]), ("Cleo", [(600, 720), (930, 970)])]
for i in range(3):
    for j in range(i + 1, 3):
        t = 0; ps = []
        for x in P[i][1]:
            for y in P[j][1]:
                lo = max(x[0], y[0]); hi = min(x[1], y[1])
                if lo < hi: t += hi - lo; ps.append(f"{lo // 60}:{lo % 60:02}-{hi // 60}:{hi % 60:02}")
        print(f"{P[i][0]} & {P[j][0]}: {', '.join(ps) if ps else 'none'} ({t} min)")
