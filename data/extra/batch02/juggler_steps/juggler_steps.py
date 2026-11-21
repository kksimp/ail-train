from math import isqrt
def jug(s):
    q = [s]; a = s
    while a != 1:
        a = isqrt(a) if a % 2 == 0 else isqrt(a ** 3); q.append(a)
    return q
for s in [3, 9, 20, 30]:
    q = jug(s); print(f"{s}: {len(q) - 1} steps, peak {max(q)}")
print("9 -> " + " ".join(map(str, jug(9))))
b = max(range(2, 30), key=lambda n: len(jug(n)))
print(f"most steps below 30: {b} ({len(jug(b)) - 1})")
