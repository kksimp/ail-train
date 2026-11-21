pupils = [("Abe", 14), ("Bea", 9), ("Cal", 17), ("Dev", 11), ("Ema", 12), ("Fin", 6), ("Gia", 15), ("Hal", 9), ("Ira", 13), ("Jon", 8), ("Kim", 16), ("Lou", 10), ("Max", 12), ("Nia", 7)]

def sizes(n, most):
    groups = (n + most - 1) // most
    base, extra = n // groups, n % groups
    return [base + 1 if i < extra else base for i in range(groups)]

ranked = sorted(pupils, key=lambda p: (-p[1], p[0]))
at = 0
for g, size in enumerate(sizes(len(ranked), 5)):
    members = ranked[at:at + size]
    print(f"group {g + 1} (levels {members[-1][1]}-{members[0][1]}): {', '.join(p[0] for p in members)}")
    at += size
print(f"{len(ranked)} pupils in {len(sizes(len(ranked), 5))} groups")
