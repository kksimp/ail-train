def digit(p):
    return "0123456789TE"[p:p + 1]

def matrix(row):
    p0 = [(p - row[0] + 12) % 12 for p in row]
    i0 = [(12 - p) % 12 for p in p0]
    return [[(i0[i] + p) % 12 for p in p0] for i in range(12)]

row = [7, 10, 2, 6, 9, 0, 4, 8, 11, 1, 3, 5]
m = matrix(row)
for r in m:
    print(" ".join(digit(p) for p in r))
ok = 0
for i in range(12):
    col = [r[i] for r in m]
    if len(set(m[i])) == 12 and len(set(col)) == 12:
        ok += 1
print(f"{ok} rows and columns hold all twelve classes")
