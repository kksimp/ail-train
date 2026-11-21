C = [("A", 7), ("B", 6), ("C", 5), ("D", 2)]; q = []; l = [c[1] for c in C]; mo = True
while mo:
    mo = False
    for i, c in enumerate(C):
        if l[i] > 0: l[i] -= 1; q.append(f"{c[0]}{c[1] - l[i]}"); mo = True
cl = 0; row = []
for i, s in enumerate(q):
    row.append(f"{s:<3}")
    if i % 5 > 0 and q[i - 1][0] == s[0]: cl += 1
    if i % 5 == 4 or i == len(q) - 1: print(" ".join(row).rstrip()); row = []
print(f"{len(q)} seated, {cl} side-by-side clashes")
