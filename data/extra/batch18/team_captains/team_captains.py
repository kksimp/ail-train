teams = [("Rovers", [(4, "Diaz"), (9, "Okoro"), (1, "Berg")], 9), ("United", [(7, "Lam"), (5, "Hart")], None), ("Athletic", [(3, "Sato"), (8, "Kane")], 10)]
def cap(t):
    if t[2] is None: return None
    for p in t[1]:
        if p[0] == t[2]: return p
    return None
for t in teams:
    c = cap(t)
    print(f"{t[0]}: captain {c[1] if c else 'no captain'}, first listed {t[1][0][1]}")
print(f"{sum(1 for t in teams if cap(t))} of {len(teams)} teams have a valid captain")
