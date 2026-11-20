def merge(sh):
    out = []
    for s in sorted(sh):
        if out and s[0] <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], s[1]))
        else:
            out.append(s)
    return out
def ov(a, b):
    return sum(max(0, min(x[1], y[1]) - max(x[0], y[0])) for x in a for y in b)
hm = lambda m: f"{m // 60}h{m % 60:02d}"
raw = {"Ola": [(540, 720), (700, 780), (900, 1020)], "Pat": [(600, 660), (660, 840)], "Rui": [(480, 500), (1000, 1100), (490, 530)]}
mg = {}
for n, sh in raw.items():
    m = merge(sh); mg[n] = m
    print(f"{n}: " + ", ".join(f"{hm(a)}-{hm(b)}" for a, b in m) + f" = {hm(sum(b - a for a, b in m))}")
print(f"Ola and Pat together: {hm(ov(mg['Ola'], mg['Pat']))}")
print(f"Ola and Rui together: {hm(ov(mg['Ola'], mg['Rui']))}")
