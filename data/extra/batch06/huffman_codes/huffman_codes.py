t = "she sells sea shells by the sea shore"; C = {}
for c in t: C[c] = C.get(c, 0) + 1
G = [(C[k], k) for k in C]; D = {k: "" for k in C}
while len(G) > 1:
    G = sorted(G); a, b = G[0], G[1]
    for ch in a[1]: D[ch] = "0" + D[ch]
    for ch in b[1]: D[ch] = "1" + D[ch]
    G = G[2:]; G.append((a[0] + b[0], a[1] + b[1]))
bt = 0
for k in sorted(C, key=lambda k: (-C[k], k)): bt += C[k] * len(D[k]); print(f"{'space' if k == ' ' else k:<5} x{C[k]:<2} {D[k]}")
print(f"{bt} bits vs {len(t) * 8} bits")
