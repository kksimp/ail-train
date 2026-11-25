import sys

def is_digits(s):
    return len(s) > 0 and all(c in "0123456789" for c in s)

def sigma(n):
    return sum(d for d in range(1, n) if n % d == 0) if n < 5000 else fast(n)

def fast(n):
    s = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            s += d
            if n // d != d:
                s += n // d
        d += 1
    return s if n > 1 else 0

p = a = f = bad = 0
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    v = int(t) if is_digits(t) and len(t) <= 9 else 0
    if v < 1 or v > 1000000:
        print(f"{t} invalid"); bad += 1; continue
    s = sigma(v)
    if s == v:
        print(f"{v} perfect {s}"); p += 1
    elif s > v:
        print(f"{v} abundant {s}"); a += 1
    else:
        print(f"{v} deficient {s}"); f += 1
print(f"perfect {p} abundant {a} deficient {f} invalid {bad}")
