W = [(3, 4), (-2, 7), (5, -1), (0, 0)]; p = (0, 0); tr = 0
for w in W:
    s = (w[0] - p[0], w[1] - p[1]); tr += abs(s[0]) + abs(s[1]); p = (p[0] + s[0], p[1] + s[1])
    print(f"to ({w[0]}, {w[1]}): step ({s[0]}, {s[1]})")
print(f"travelled {tr}, final ({p[0]}, {p[1]}), negated (-3, 4)")
