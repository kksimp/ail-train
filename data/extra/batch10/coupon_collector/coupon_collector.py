def expected(n):
    h = 0.0
    for k in range(1, n + 1):
        h += 1.0 / float(k)
    return float(n) * h

seed = 2024
def below(n):
    global seed
    seed = (seed * 1103515245 + 12345) % 2147483648
    return (seed // 65536) % n

def trial(n):
    seen = set()
    draws = 0
    while len(seen) < n:
        seen.add(below(n))
        draws += 1
    return draws

for n in [2, 6, 10, 20]:
    runs = 2000
    total = 0
    most = 0
    for _ in range(runs):
        d = trial(n)
        total += d
        if d > most:
            most = d
    avg = float(total) / float(runs)
    print(f"{n:>2} kinds: expected {expected(n):.2f}, simulated {avg:.2f}, worst run {most}")
print(f"collecting 50 kinds takes about {expected(50):.1f} draws")
