def ripple(xs):
    n = len(xs)
    return [(xs[(i + n - 1) % n] + 2 * xs[i] + xs[(i + 1) % n]) % 4 for i in range(n)]

g = ".-+#"
xs = [1 if i == 12 else 0 for i in range(25)]
for t in range(10):
    print(f"{t:>2} {''.join(g[v] for v in xs)}")
    xs = ripple(xs)
for t in range(10, 40):
    xs = ripple(xs)
alive = sum(1 for v in xs if v != 0)
print(f"after 40 steps: {alive} of 25 cells are not zero, total {sum(xs)}")
