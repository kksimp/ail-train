T = [[0, 3, 1, 7, 5, 9, 8, 6, 4, 2], [7, 0, 9, 2, 1, 5, 4, 8, 6, 3], [4, 2, 0, 6, 8, 7, 1, 3, 5, 9], [1, 7, 5, 0, 9, 8, 3, 4, 2, 6], [6, 1, 2, 3, 0, 4, 5, 9, 7, 8], [3, 6, 7, 4, 2, 0, 9, 5, 8, 1], [5, 8, 6, 9, 7, 2, 0, 1, 3, 4], [8, 9, 4, 5, 3, 6, 2, 0, 1, 7], [9, 4, 3, 8, 6, 1, 7, 2, 0, 5], [2, 5, 8, 1, 4, 3, 6, 7, 9, 0]]

def interim(digits):
    v = 0
    for d in digits:
        v = T[v][d]
    return v

for num in [[5, 7, 2], [1, 2, 3, 4, 5], [9, 8, 7, 6], [2, 0, 2, 6, 1, 1]]:
    c = interim(num)
    shown = "".join(str(d) for d in num)
    print(f"{shown} -> check digit {c}, full number {shown}{c}")
base = [3, 1, 4, 1, 5, 9, 2, 6]
full = base + [interim(base)]
swaps = 0
caught = 0
for i in range(len(full) - 1):
    if full[i] != full[i + 1]:
        bad = list(full)
        bad[i], bad[i + 1] = bad[i + 1], bad[i]
        swaps += 1
        if interim(bad) != 0:
            caught += 1
typos = 0
spotted = 0
for i in range(len(full)):
    for d in range(10):
        if d != full[i]:
            bad = list(full)
            bad[i] = d
            typos += 1
            if interim(bad) != 0:
                spotted += 1
fs = "".join(str(d) for d in full)
print(f"{fs}: {caught} of {swaps} neighbour swaps and {spotted} of {typos} typos caught")
