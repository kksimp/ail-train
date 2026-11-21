def parse(line):
    a, b, t = line.split(" ")
    lo, hi = a.split("-")
    return (int(lo), int(hi), b[0], t)

def by_count(p):
    lo, hi, c, t = p
    return lo <= t.count(c) <= hi

def by_place(p):
    lo, hi, c, t = p
    a = (t[lo - 1] if lo - 1 < len(t) else ' ') == c
    b = (t[hi - 1] if hi - 1 < len(t) else ' ') == c
    return a != b

def tf(b):
    return "true" if b else "false"

lines = ["2-4 k: kkbqk", "1-3 m: amzmm", "3-5 t: ttxtq", "2-2 p: ppp", "1-6 r: arrrrr", "4-5 z: qqqzq"]
policies = [parse(l) for l in lines]
for p in policies:
    print(f"{p[3]:<7} {p[2]} {p[0]}-{p[1]}: count {tf(by_count(p))}, place {tf(by_place(p))}")
print(f"part 1: {sum(1 for p in policies if by_count(p))} labels pass the count policy")
print(f"part 2: {sum(1 for p in policies if by_place(p))} labels pass the place policy")
