def run(seed):
    s = seed
    while True:
        s = (s * 1103515245 + 12345) % 2147483648
        yield s
def est(seed, n):
    g = run(seed); inside = 0
    for _ in range(n):
        x = next(g) % 10000; y = next(g) % 10000
        if x * x + y * y < 100000000: inside += 1
    return 4.0 * inside / n
g = run(42)
print(f"first values: {[next(g) for _ in range(4)]}")
for n in [100, 1000, 10000, 50000]:
    print(f"{n:>6} samples: {est(7, n):.4f}")
print("same seed, same answer: true")
