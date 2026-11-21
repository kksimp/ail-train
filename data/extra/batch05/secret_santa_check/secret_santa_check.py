for d in [[("A", "B"), ("B", "C"), ("C", "A"), ("D", "E"), ("E", "D")], [("A", "B"), ("B", "B"), ("C", "A"), ("D", "C")], [("A", "C"), ("B", "C"), ("C", "D"), ("D", "A")]]:
    pr = []; G = [p[0] for p in d]; T = [p[1] for p in d]
    for g, t in d:
        if g == t: pr.append(f"{g} draws self")
    for t in T:
        if T.count(t) > 1 and f"{t} drawn twice" not in pr: pr.append(f"{t} drawn twice")
    for g in G:
        if g not in T: pr.append(f"{g} gets nothing")
    if not pr:
        sn = set(); cy = []
        for g in G:
            if g in sn: continue
            ln = []; c = g
            while c not in sn: sn.add(c); ln.append(c); c = dict(d)[c]
            cy.append(">".join(ln))
        print(f"ok: {' + '.join(cy)}")
    else: print(f"problems: {'; '.join(pr)}")
