def sl(t):
    o = ""; d = False
    for c in t.lower():
        if c.isalnum():
            if d and o: o += "-"
            o += c; d = False
        else: d = True
    return o
u = {}
for t in ["Hello, World!", "  AIL 0.2 is out  ", "Tips & Tricks: Part 2", "Hello World", "C'est la vie"]:
    b = sl(t); u[b] = u.get(b, 0) + 1; n = u[b]; print(f"{t.strip()} => {b if n == 1 else f'{b}-{n}'}")
