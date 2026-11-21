L = 1000; how = {}; b = 2
while b * b < L:
    v = b * b; e = 2
    while v < L:
        if v not in how: how[v] = f"{b}^{e}"
        v *= b; e += 1
    b += 1
o = sorted(how)
print(f"{len(o)} perfect powers below {L}")
print(" ".join(f"{v}={how[v]}" for v in o[:15]))
print(f"squares listed: {sum(1 for v in o if how[v].endswith('^2'))}, sixth powers: {[v for v in o if v in (64, 729)]}")
