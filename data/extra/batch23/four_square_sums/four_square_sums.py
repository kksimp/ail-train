def isqrt(x):
    r = 0
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r

def find(n):
    top = isqrt(n)
    for a in range(0, top + 1):
        for b in range(0, a + 1):
            for c in range(0, b + 1):
                rest = n - a * a - b * b - c * c
                d = isqrt(max(rest, 0))
                if rest >= 0 and d * d == rest and d <= c:
                    return [a, b, c, d]
    return [0]

def r4(n):
    s = isqrt(n)
    low = -s
    ways = 0
    for a in range(low, s + 1):
        for b in range(low, s + 1):
            for c in range(low, s + 1):
                rest = n - a * a - b * b - c * c
                d = isqrt(max(rest, 0))
                if rest >= 0 and d * d == rest:
                    ways += 1 if d == 0 else 2
    return ways

def three_squares(n):
    top3 = isqrt(n)
    for a in range(0, top3 + 1):
        for b in range(0, a + 1):
            rest = n - a * a - b * b
            c = isqrt(max(rest, 0))
            if rest >= 0 and c * c == rest:
                return True
    return False

def jacobi_count(n):
    total = 0
    for d in range(1, n + 1):
        if n % d == 0 and d % 4 != 0:
            total += d
    return 8 * total

for n in [1, 7, 15, 30, 100, 127, 310]:
    sq = find(n)
    print(f"{n:>3} = {sq[0]}^2 + {sq[1]}^2 + {sq[2]}^2 + {sq[3]}^2, r4 = {r4(n)}, Jacobi {jacobi_count(n)}")
needs_four = []
for n in range(1, 60):
    if not three_squares(n):
        needs_four.append(n)
print(f"below 60, three squares are not enough for: {needs_four}")
