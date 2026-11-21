rows = ["SERT", "TAEL", "OPIN", "DRAC"]; used = [False] * 16
def trace(w, k, r, c):
    if r < 0 or r > 3 or c < 0 or c > 3: return False
    if used[r * 4 + c] or rows[r][c] != w[k]: return False
    if k == len(w) - 1: return True
    used[r * 4 + c] = True
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr != 0 or dc != 0) and trace(w, k + 1, r + dr, c + dc): used[r * 4 + c] = False; return True
    used[r * 4 + c] = False; return False
def found(w): return any(trace(w, 0, r, c) for r in range(4) for c in range(4))
def pts(n): return 1 if n <= 4 else 2 if n == 5 else 3 if n == 6 else 5
tot = 0
for w in ["SEAT", "TEAL", "PAIN", "RAIN", "PLAIN", "STAR", "TAPIR", "OPAL", "SEATED", "LINE", "CARD", "PATIO"]:
    if found(w): p = pts(len(w)); tot += p; print(f"{w:<7} yes, {p} pt")
    else: print(f"{w:<7} not on the grid")
print(f"score {tot}")
