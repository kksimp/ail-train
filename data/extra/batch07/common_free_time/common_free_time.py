B = [[(540, 600), (720, 780), (900, 960)], [(570, 630), (660, 690), (960, 1020)], [(600, 615), (750, 840), (990, 1000)]]
A = sorted(x for p in B for x in p); M = []
for b in A:
    if M and b[0] <= M[-1][1]: M[-1] = (M[-1][0], max(b[1], M[-1][1]))
    else: M.append(b)
h = lambda m: f"{m // 60:02}:{m % 60:02}"; t = 540
for m in M:
    if m[0] - t >= 30: print(f"free {h(t)}-{h(m[0])} ({m[0] - t} min)")
    if m[1] > t: t = m[1]
if 1020 - t >= 30: print(f"free {h(t)}-{h(1020)} ({1020 - t} min)")
print(f"{len(M)} busy blocks after merging")
