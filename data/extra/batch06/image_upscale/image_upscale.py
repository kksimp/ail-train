def up(I, k): return [r for row in I for r in ["".join(c * k for c in row)] * k]
def dn(I, k): return ["".join(I[y][x] for x in range(0, len(I[y]), k)) for y in range(0, len(I), k)]
I = [".#.", "###", "#.#"]
for k in [2, 3]:
    B = up(I, k); print(f"x{k}:")
    for l in B: print(l)
    print(f"round trip ok: {'true' if dn(B, k) == I else 'false'}")
