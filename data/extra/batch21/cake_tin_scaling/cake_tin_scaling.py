PI = 3.141592653589793

def area(t):
    kind, n = t
    if kind == "r":
        return PI * (float(n) / 2.0) * (float(n) / 2.0)
    return float(n) * float(n)

def label(t):
    return f"{t[1]} cm round" if t[0] == "r" else f"{t[1]} cm square"

base = area(("r", 20))
recipe = [("butter", 225), ("sugar", 225), ("flour", 225), ("milk", 30)]
tins = [("r", 15), ("r", 23), ("s", 20), ("s", 23), ("r", 25)]
for t in tins:
    f = area(t) / base
    parts = []
    for name, g in recipe:
        scaled = int(round(float(g) * f / 5.0)) * 5
        parts.append(f"{name} {scaled}")
    eggs = max(int(round(4.0 * f)), 1)
    print(f"{label(t):<13} x{f:.4f}: {', '.join(parts)}, eggs {eggs}")
