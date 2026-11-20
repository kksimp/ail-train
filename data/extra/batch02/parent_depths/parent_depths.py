par = [-1, 0, 0, 1, 1, 2, 4, 4, 6, 2]
def depth(i): return 0 if par[i] < 0 else depth(par[i]) + 1
d = [depth(i) for i in range(len(par))]
print("depths: " + " ".join(map(str, d)))
h = max(d); print(f"height: {h}")
for l in range(h + 1):
    print(f"level {l}: " + " ".join(str(i) for i in range(len(par)) if d[i] == l))
print("leaves: " + " ".join(str(i) for i in range(len(par)) if i not in par))
