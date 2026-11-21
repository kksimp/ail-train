L = 20000
s = [0] * L
for i in range(1, L):
    for m in range(2 * i, L, i): s[m] += i
pairs, perf = [], []
for a in range(2, L):
    b = s[a]
    if b == a: perf.append(a)
    elif a < b < L and s[b] == a: pairs.append(f"({a}, {b})")
print(f"amicable below {L}: {' '.join(pairs)}")
print("perfect: " + " ".join(map(str, perf)))
ab = [n for n in range(1, 100) if s[n] > n]
print(f"abundant below 100: {len(ab)}, first {' '.join(map(str, ab[:5]))}")
