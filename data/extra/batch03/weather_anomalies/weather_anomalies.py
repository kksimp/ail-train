t = [112, 118, 121, 115, 109, 117, 120, 158, 119, 113, 71, 116, 122, 125, 89, 121]
def sh(x): return ("-" if x < 0 else "") + f"{abs(x) // 10}.{abs(x) % 10}"
f = 0
for i in range(7, len(t)):
    m = sum(t[i - 7:i]) // 7; d = t[i] - m
    if abs(d) > 30: f += 1; print(f"day {i + 1}: {sh(t[i])} vs mean {sh(m)} ({sh(d)})")
print(f"{f} unusual days of {len(t) - 7} checked")
