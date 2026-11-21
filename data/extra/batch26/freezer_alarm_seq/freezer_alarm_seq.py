def temps(seed):
    x = seed; t = -190
    while True:
        x = (x * 75 + 74) % 65537
        t += x % 7 - 3
        yield t
def tenths(v):
    s = "-" if v < 0 else ""
    a = abs(v)
    return f"{s}{a // 10}.{a % 10}"
for name, seed in [("chest", 11), ("upright", 99), ("display", 2024)]:
    g = temps(seed); v = [next(g) for _ in range(48)]
    print(f"{name:<8} coldest {tenths(min(v))} C, warmest {tenths(max(v))} C")
    i = next((k for k, t in enumerate(v) if t > -180), None)
    if i is not None:
        m = i * 30
        print(f"  alarm at {m // 60:02}:{m % 60:02}")
    else:
        print("  no alarm today")
