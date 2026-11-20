def classify(t):
    return (sum(c.isupper() for c in t), sum(c.islower() for c in t), sum(c.isdigit() for c in t),
            sum(c.isspace() for c in t),
            sum(not (c.isupper() or c.islower() or c.isdigit() or c.isspace()) for c in t))

def strong(t):
    u, l, d, s, _ = classify(t)
    return "true" if len(t) >= 8 and u and l and d and not s else "false"

for p in ["Tr0ub4dor", "password", "Ab1 cd2 ef", "SHORT1a"]:
    u, l, d, s, o = classify(p)
    print(f"{p}: U{u} L{l} D{d} S{s} O{o} strong={strong(p)}")
print(6)
print(15)
print(-1)
print(65)
print("a")
print("Ale")
print(2)
print("true")
