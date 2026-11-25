import sys

def is_digits(s):
    return len(s) > 0 and all(c in "0123456789" for c in s)

best = None
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    v = int(t) if is_digits(t) and len(t) <= 9 else 0
    if v < 1 or v > 1000000:
        print(f"{t} invalid"); continue
    n, steps, peak = v, 0, v
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
        peak = max(peak, n)
    print(f"{v} steps {steps} peak {peak}")
    if best is None or steps > best[1] or (steps == best[1] and v < best[0]):
        best = (v, steps)
print("longest none" if best is None else f"longest {best[0]} steps {best[1]}")
