def cell(t, r, c):
    if r < 0 or r >= len(t) or c < 0 or c >= len(t[0]): return 20
    return t[r][c]

t = [[1400 if r == 2 else 1100 for c in range(7)] for r in range(5)]
st = [[0]*7 for r in range(5)]
step = 0
crust = 0
while crust < 35:
    step += 1
    nxt = [row[:] for row in t]
    for r in range(5):
        for c in range(7):
            if st[r][c] == 0:
                v = (2 * t[r][c] + cell(t, r-1, c) + cell(t, r+1, c) + cell(t, r, c-1) + cell(t, r, c+1)) // 6
                nxt[r][c] = v
                if v < 600:
                    st[r][c] = step
                    crust += 1
    t = nxt
    if step % 4 == 0 or crust == 35:
        print(f"step {step}: {crust} crust cells, centre at {t[2][3]}")
print("step each cell set:")
for r in range(5):
    print("".join(f"{s:>3}" for s in st[r]))
