def r5(c): r = c % 5; return c - r if r < 3 else c + 5 - r
def ce(c): return f"{c // 100}.{c % 100:02}"
d = 0; T = [1001, 1002, 1003, 1004, 1005, 1236, 999, 4572]
for t in T: r = r5(t); d += r - t; print(f"{ce(t)} -> cash {ce(r)} ({'+' if r - t > 0 else ''}{r - t})")
print(f"net rounding over {len(T)} sales: {d} cents")
