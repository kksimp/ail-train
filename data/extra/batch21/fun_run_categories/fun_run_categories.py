runners = [("Aled", [1986, 5, 17], 1405), ("Bryn", [1986, 5, 18], 1388), ("Cerys", [2010, 1, 3], 1622), ("Dafydd", [1974, 11, 30], 1517), ("Efa", [1961, 2, 14], 1764), ("Ffion", [1999, 8, 9], 1352), ("Gwen", [1972, 3, 21], 1490), ("Huw", [2009, 5, 17], 1580)]

def age_on(by, bm, bd, y, m, d):
    before = m < bm or (m == bm and d < bd)
    return y - by - 1 if before else y - by

def category(age):
    if age < 18:
        return "Junior"
    if age < 40:
        return "Senior"
    if age < 50:
        return "V40"
    if age < 60:
        return "V50"
    return "V60"

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

best = {}
for i, (name, born, secs) in enumerate(runners):
    age = age_on(born[0], born[1], born[2], 2026, 5, 17)
    cat = category(age)
    print(f"{name:<7} age {age:>2} {cat:<6} {mmss(secs)}")
    cur = best.get(cat, -1)
    if cur < 0 or secs < runners[cur][2]:
        best[cat] = i
for cat in ["Junior", "Senior", "V40", "V50", "V60"]:
    if cat in best:
        print(f"{cat} winner: {runners[best[cat]][0]}")
f = min(runners, key=lambda r: r[2])
print(f"overall: {f[0]} in {mmss(f[2])}")
