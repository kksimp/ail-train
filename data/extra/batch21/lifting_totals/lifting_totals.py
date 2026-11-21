lifters = [("Ana", 588, [80, -84, 84], [100, 104, -107]), ("Bea", 579, [-82, 82, -86], [102, 106, -110]), ("Cai", 601, [78, 81, 83], [-100, -100, -100]), ("Dan", 594, [85, -88, -88], [105, -109, 109]), ("Eva", 590, [79, 82, -85], [98, 101, 103])]

def best(xs):
    good = [x for x in xs if x > 0]
    return max(good) if good else 0

def total(l):
    s, c = best(l[2]), best(l[3])
    return 0 if s == 0 or c == 0 else s + c

ranked = sorted(lifters, key=lambda l: (-total(l), l[1]))
place = 1
for l in ranked:
    kg = f"{l[1] // 10}.{l[1] % 10}"
    if total(l) == 0:
        print(f"--  {l[0]:<4} ({kg} kg) bombed out")
    else:
        print(f"{place}.  {l[0]:<4} ({kg} kg) {best(l[2])} + {best(l[3])} = {total(l)}")
        place += 1
made = sum(sum(1 for x in l[2] if x > 0) + sum(1 for x in l[3] if x > 0) for l in lifters)
print(f"{made} of {len(lifters) * 6} attempts were good lifts")
