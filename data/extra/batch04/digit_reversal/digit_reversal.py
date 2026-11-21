rv = lambda n: int(str(n)[::-1])
def ip(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
for n in [1234, 1200, 9, 8712, 9801]:
    r = rv(n); print(f"{n} -> {r}" + (f" (reversal is {r // n} times it)" if r != n and r % n == 0 else ""))
print(f"emirps below 200: {[n for n in range(10, 200) if ip(n) and ip(rv(n)) and rv(n) != n]}")
print(f"4-digit numbers dividing their reversal: {[n for n in range(1000, 10000) if rv(n) != n and rv(n) % n == 0]}")
