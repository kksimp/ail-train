P = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "D": 1.0, "F": 0.0}
for name, cs in [("Iris", [("A", 4), ("B+", 3), ("A-", 3)]), ("Jon", [("C", 4), ("B", 4), ("F", 2)]), ("Kai", [("A", 1), ("E", 3)]), ("Lea", [])]:
    w, cr, ok = 0.0, 0, True
    for g, c in cs:
        if g not in P: ok = False; break
        w += P[g] * float(c); cr += c
    if ok and cr:
        print(f"{name}: {w / cr:.2f}")
    else:
        print(f"{name}: no GPA")
