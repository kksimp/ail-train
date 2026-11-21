L = 1000
d = [0] * (L + 1)
for i in range(1, L + 1):
    for m in range(i, L + 1, i): d[m] += 1
print("1..12: " + " ".join(str(d[n]) for n in range(1, 13)))
best, rec = 0, []
for n in range(1, L + 1):
    if d[n] > best: best = d[n]; rec.append(f"{n}({d[n]})")
print("records: " + " ".join(rec))
print(f"primes: {sum(1 for n in range(2, L + 1) if d[n] == 2)}, odd divisor counts (squares): {sum(1 for n in range(1, L + 1) if d[n] % 2 == 1)}")
