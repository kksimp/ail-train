s = 12345
def roll():
    global s
    s = (s * 75 + 74) % 65537
    return s % 6 + 1
tot = []
for _ in range(3600):
    a = roll(); b = roll(); tot.append(a + b)
c = {}
for t in tot: c[t] = c.get(t, 0) + 1
most = max(c.values())
for t in range(2, 13):
    n = c.get(t, 0)
    print(f"{t:>2} {n:>4} " + "*" * (n * 40 // most))
print(f"sevens: {c.get(7, 0) * 100 // 3600}%")
