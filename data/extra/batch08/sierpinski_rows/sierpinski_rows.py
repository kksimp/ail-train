st = 0
for r in range(16):
    cells = []
    for c in range(r + 1):
        if (r & c) == c: cells.append("*"); st += 1
        else: cells.append(" ")
    print(" " * (15 - r) + " ".join(cells))
print(f"{st} odd entries in 16 rows")
