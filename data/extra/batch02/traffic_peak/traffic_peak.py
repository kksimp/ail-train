c = [12, 18, 25, 40, 66, 81, 77, 59, 44, 38, 35, 41, 50, 47, 30, 22]
st = lambda i: f"{(360 + i * 15) // 60:02d}:{(360 + i * 15) % 60:02d}"
s = [sum(c[i:i + 4]) for i in range(len(c) - 3)]
b = 0
for i in range(1, len(s)):
    if s[i] > s[b]: b = i
print(f"busiest hour: {st(b)}-{st(b + 4)} with {s[b]} cars")
q = c.index(min(c))
print(f"quietest slot: {st(q)} ({c[q]})")
for h in range(0, len(c), 4):
    t = sum(c[h:h + 4])
    print(f"{st(h)} {t:>4} {'=' * (t // 10)}")
print(f"rising steps: {sum(1 for i in range(1, len(c)) if c[i] > c[i - 1])} of {len(c) - 1}")
