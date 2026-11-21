def gen(o, c, p, out):
    if o == 0 and c == 0: out.append(p); return
    if o > 0: gen(o - 1, c, p + "(", out)
    if c > o: gen(o, c - 1, p + ")", out)
t = []; gen(3, 3, "", t)
print(f"3 pairs: {' '.join(t)}")
for n in range(1, 9):
    o = []; gen(n, n, "", o); print(f"{n} pairs: {len(o)}")
