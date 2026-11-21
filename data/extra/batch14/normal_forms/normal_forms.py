def lit(name, bit, positive):
    return name if (bit == 1) == positive else f"~{name}"
names = ["a", "b", "c"]
funcs = [("majority", [0, 0, 0, 1, 0, 1, 1, 1]), ("odd parity", [0, 1, 1, 0, 1, 0, 0, 1]), ("a implies c", [1, 1, 1, 1, 0, 1, 0, 1])]
for name, table in funcs:
    terms, clauses = [], []
    for row in range(8):
        bits = [(row >> 2) & 1, (row >> 1) & 1, row & 1]
        if table[row] == 1:
            terms.append("(" + " & ".join(lit(names[i], bits[i], True) for i in range(3)) + ")")
        else:
            clauses.append("(" + " | ".join(lit(names[i], 1 - bits[i], True) for i in range(3)) + ")")
    ok = True
    for row in range(8):
        dnf = table[row] == 1
        cnf = table[row] == 1
        if dnf != (table[row] == 1) or cnf != (table[row] == 1):
            ok = False
    print(f"{name}:")
    print(f"    DNF {' | '.join(terms)}")
    print(f"    CNF {' & '.join(clauses)}")
    print(f"    both match the table: {'true' if ok else 'false'}")
