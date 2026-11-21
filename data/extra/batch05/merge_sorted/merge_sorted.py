def m2(a, b):
    o = []; i = j = c = 0
    while i < len(a) and j < len(b):
        c += 1
        if a[i] <= b[j]: o.append(a[i]); i += 1
        else: o.append(b[j]); j += 1
    return o + a[i:] + b[j:], c
L = [[1, 9, 14, 30], [2, 3, 22], [5, 6, 7, 8, 40], [4, 18]]; acc = []; t = 0
for l in L: acc, c = m2(acc, l); t += c
print("pairwise: " + " ".join(map(str, acc))); print(f"comparisons: {t}")
ix = [0] * 4; o = []; kc = 0
while len(o) < len(acc):
    p = -1
    for k in range(4):
        if ix[k] < len(L[k]):
            if p >= 0: kc += 1
            if p < 0 or L[k][ix[k]] < L[p][ix[p]]: p = k
    o.append(L[p][ix[p]]); ix[p] += 1
print(f"k-way same: {'true' if o == acc else 'false'}, comparisons: {kc}")
