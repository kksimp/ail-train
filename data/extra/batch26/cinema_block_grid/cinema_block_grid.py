plan = ["xx..x....x", "x.xx..xxxx", "..........", "xxxx...xxx", "..x.x.x.x."]
hall = [[1 if c == "x" else 0 for c in s] for s in plan]
def find(n):
    for r in range(len(hall)):
        run = 0
        for c in range(len(hall[r])):
            run = run + 1 if hall[r][c] == 0 else 0
            if run == n: return (r, c - n + 1)
    return None
for n in [4, 6, 3, 2, 5]:
    s = find(n)
    if s is None:
        print(f"group of {n}: no block free"); continue
    r, st = s
    for c in range(st, st + n): hall[r][c] = 1
    print(f"group of {n}: row {chr(65 + r)} seats {st + 1}-{st + n}")
for row in hall:
    print("".join("x" if v == 1 else "." for v in row))
print(f"free seats left: {sum(1 for row in hall for v in row if v == 0)}")
