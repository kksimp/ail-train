deltas = [3, 5, 4, -2, 6, -1, -7, 2, -6, -4]
level = 0
for i, d in enumerate(deltas):
    level += d
    mins = 19 * 60 + i * 15
    mark = " over limit" if level > 15 else ""
    print(f"{mins // 60}:{mins % 60:02} {d:>3} -> {level:>2}{mark}")
cur = 0; peak = 0
for d in deltas:
    cur += d; peak = max(cur, peak)
print(f"coats handed in {sum(d for d in deltas if d > 0)}, peak {peak} on 15 hangers, {cur} left at close")
