def isp(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
ps = [n for n in range(2, 1000) if isp(n)]
print(" ".join(map(str, ps[:12])))
print(" ".join(map(str, [p for p in ps if p % 10 == 3][:5])))
tw, prev = [], 0
for p in ps:
    if p > 200: break
    if p - prev == 2: tw.append(f"({prev},{p})")
    prev = p
print(f"twin pairs below 200: {len(tw)}")
print(" ".join(tw[:6]))
print(f"[{ps[99]}]")
