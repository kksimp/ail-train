q = [("adult",), ("child", 3), ("child", 9), ("student", "ISIC-77812"), ("student", "LIB-201"), ("group", 12), ("member", 5531), ("group", 4)]
def price(v):
    k = v[0]
    if k == "adult": return 1600
    if k == "child": return 0 if v[1] < 5 else 800
    if k == "student": return 1000 if v[1].startswith("ISIC") else 1600
    if k == "group": return v[1] * 1200 if v[1] >= 10 else v[1] * 1600
    return 0
t = 0; ppl = 0
for v in q:
    p = price(v); t += p; h = v[1] if v[0] == "group" else 1; ppl += h
    print(f"{h:>2} visitor(s): {p // 100}.{p % 100:02}")
print(f"{ppl} people, takings {t // 100}.{t % 100:02}")
