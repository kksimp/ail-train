def ln(c):
    v = c / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
def lu(h): return 0.2126 * ln(int(h[1:3], 16)) + 0.7152 * ln(int(h[3:5], 16)) + 0.0722 * ln(int(h[5:7], 16))
def ra(a, b): x, y = lu(a), lu(b); return (max(x, y) + 0.05) / (min(x, y) + 0.05)
for a, b in [("#000000", "#ffffff"), ("#777777", "#ffffff"), ("#1a5fb4", "#ffffff"), ("#ffcc00", "#ffffff"), ("#ffcc00", "#222222"), ("#2e7d32", "#e8f5e9")]:
    r = ra(a, b); print(f"{a} on {b}: {r:.2f}:1 {'pass' if r >= 4.5 else 'fail'}")
