def so(w):
    i = 0
    while i < len(w):
        c = w[i]
        if c in "aeiou" or (c == "y" and i > 0): break
        i += 1
    return w[:i], w[i:]
for a, b in [("bad", "salad"), ("crushing", "blow"), ("light", "fire"), ("shy", "tray"), ("eat", "pie")]:
    ao, ar = so(a); bo, br = so(b)
    print(f"{a} {b} -> {bo}{ar} {ao}{br}")
