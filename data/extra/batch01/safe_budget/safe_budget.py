MAX = 2**63 - 1
def total(lines):
    s = 0
    for q, u in lines:
        c = q * u
        if c > MAX: return None
        s += c
        if s > MAX: return None
    return s
budgets = [("office", [(3, 1200), (10, 45)]), ("rockets", [(2, 4000000000000000000), (1, 3000000000000000000)]), ("atoms", [(9000000000, 9000000000)]), ("empty", [])]
for name, lines in budgets:
    t = total(lines)
    print(f"{name}: {t:,}" if t is not None else f"{name}: too large to count")
print("true")
print(MAX - 1)
print("true")
print("true")
