G = ["Amy", "Bob", "Cal", "Dot", "Eve", "Fin", "Gil", "Hal", "Ivy", "Jo"]; F = [("Amy", "Bob"), ("Cal", "Dot"), ("Amy", "Eve"), ("Fin", "Gil"), ("Bob", "Hal"), ("Ivy", "Amy")]; T = []
for g in G:
    for t in T:
        if len(t) < 4 and not any((g, o) in F or (o, g) in F for o in t): t.append(g); break
    else: T.append([g])
for i, t in enumerate(T): print(f"table {i + 1}: {', '.join(t)}")
