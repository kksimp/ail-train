h = lambda m: f"{m // 60:02}:{m % 60:02}"; c = 540; b = 0
for n, m in [("report", 60), ("email", 20), ("slides", 75), ("review", 30)]:
    l = m
    while l > 0:
        w = min(l, 25); print(f"{h(c)}-{h(c + w)} {n}"); c += w; l -= w; b += 1; c += 20 if b % 4 == 0 else 5
print(f"{b} blocks, done by {h(c)}")
