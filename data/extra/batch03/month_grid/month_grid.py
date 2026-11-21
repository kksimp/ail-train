def leap(y): return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
def din(y, m): return (29 if leap(y) else 28) if m == 2 else 30 if m in (4, 6, 9, 11) else 31
def grid(f, n):
    out = ["Mo Tu We Th Fr Sa Su"]; row = ["  "] * f
    for d in range(1, n + 1):
        row.append(f"{d:>2}")
        if len(row) == 7: out.append(" ".join(row)); row = []
    if row: out.append(" ".join(row))
    return out
print("February 2028 (starts Tuesday):")
for l in grid(1, din(2028, 2)): print(l)
print("September 2026 (starts Tuesday):")
for l in grid(1, din(2026, 9)): print(l)
print("leap: " + " ".join(f"{y}={str(leap(y)).lower()}" for y in [1900, 2000, 2024, 2026, 2100]))
