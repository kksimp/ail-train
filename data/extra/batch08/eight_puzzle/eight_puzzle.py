def solve(s):
    goal = "123456780"; came = {s: ""}; how = {}; q = [s]; h = 0
    while h < len(q):
        u = q[h]; h += 1
        if u == goal: break
        b = u.index("0"); r, c = divmod(b, 3)
        for dr, dc, m in [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]:
            nr = r + dr; nc = c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                l = list(u); j = nr * 3 + nc; l[b], l[j] = l[j], l[b]; v = "".join(l)
                if v not in came: came[v] = u; how[v] = m; q.append(v)
    mv = []; v = goal
    while v != s: mv.append(how[v]); v = came[v]
    mv.reverse()
    return f"{len(mv)} moves {''.join(mv)}, {len(came)} boards seen"
for s in ["123405786", "123456708", "023145786", "413726580", "182043765"]: print(f"{s}: {solve(s)}")
