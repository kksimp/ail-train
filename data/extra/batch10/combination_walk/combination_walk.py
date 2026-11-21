def next_comb(c, n):
    k = len(c)
    i = k - 1
    while i >= 0 and c[i] == n - k + i + 1:
        i -= 1
    if i < 0:
        return False
    c[i] += 1
    for j in range(i + 1, k):
        c[j] = c[j - 1] + 1
    return True

def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r

c = [1, 2, 3]
listed = [str(c)]
while next_comb(c, 5):
    listed.append(str(c))
print(f"3 of 5: {' '.join(listed)}")
for n, k in [[10, 4], [12, 6], [20, 3]]:
    d = list(range(1, k + 1))
    count = 1
    while next_comb(d, n):
        count += 1
    print(f"{k} of {n}: walked {count}, formula {binom(n, k)}")
e = [1, 2, 3]
lines = []
while True:
    if sum(e) == 15:
        lines.append(f"{e[0]}{e[1]}{e[2]}")
    if not next_comb(e, 9):
        break
print(f"3-subsets of 1..9 summing to 15: {' '.join(lines)} ({len(lines)}, the lines of a magic square)")
