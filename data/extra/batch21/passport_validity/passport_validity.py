def month_len(y, m):
    if m == 2:
        return 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28
    return 30 if m in (4, 6, 9, 11) else 31

def add_months(d, k):
    t = d[0] * 12 + d[1] - 1 + k
    y, m = t // 12, t % 12 + 1
    return [y, m, min(d[2], month_len(y, m))]

def key(d):
    return d[0] * 10000 + d[1] * 100 + d[2]

def show(d):
    return f"{d[0]}-{d[1]:02d}-{d[2]:02d}"

expiry = {"Ruth": [2027, 2, 28], "Sean": [2026, 12, 31], "Tara": [2027, 8, 31]}
rule = {"Thailand": 6, "Norway": 3, "Egypt": 6, "Ireland": 0, "Japan": 0}
trips = [("Ruth", "Thailand", [2026, 8, 31]), ("Ruth", "Norway", [2026, 11, 30]), ("Sean", "Egypt", [2026, 7, 4]), ("Sean", "Ireland", [2026, 12, 20]), ("Tara", "Japan", [2027, 8, 31]), ("Tara", "Egypt", [2027, 3, 31])]
renew = set()
for who, country, back in trips:
    need = add_months(back, rule[country])
    has = expiry[who]
    ok = key(has) >= key(need)
    if not ok:
        renew.add(who)
    print(f"{who} to {country}: back {show(back)}, needs {show(need)}, expires {show(has)}: {'ok' if ok else 'RENEW'}")
print(f"renew before travelling: {', '.join(sorted(renew))}")
