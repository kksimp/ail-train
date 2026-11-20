c = [1]
for i in range(1, 16):
    c.append(sum(c[j] * c[i - 1 - j] for j in range(i)))
print(" ".join(map(str, c)))
def bal(n):
    out = []
    def go(o, cl, cur):
        if len(cur) == 2 * n:
            out.append(cur); return
        if o < n: go(o + 1, cl, cur + "(")
        if cl < o: go(o, cl + 1, cur + ")")
    go(0, 0, "")
    return out
for n in range(7):
    print(f"n={n}: {len(bal(n))} generated, formula {c[n]}")
print(" ".join(bal(3)))
