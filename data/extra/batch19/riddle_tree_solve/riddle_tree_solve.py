def ev(m, name):
    p = m[name].split(" ")
    if len(p) == 1: return int(p[0])
    a = ev(m, p[0]); b = ev(m, p[2])
    if p[1] == "+": return a + b
    if p[1] == "-": return a - b
    if p[1] == "*": return a * b
    return a // b

def holds(m, name):
    if name == "you": return True
    p = m[name].split(" ")
    return len(p) == 3 and (holds(m, p[0]) or holds(m, p[2]))

def solve(m, name, target):
    if name == "you": return target
    p = m[name].split(" ")
    if holds(m, p[0]):
        r = ev(m, p[2])
        t = {"+": target - r, "-": target + r, "*": target // r}.get(p[1], target * r)
        return solve(m, p[0], t)
    l = ev(m, p[0])
    t = {"+": target - l, "-": l - target, "*": target // l}.get(p[1], l // target if target else 0)
    return solve(m, p[2], t)

lines = ["root: fir + elm", "fir: oak * kit", "oak: you - two", "you: 11", "two: 2", "kit: 4", "elm: pine / sev", "pine: hub + yew", "hub: cat * dot", "cat: 6", "dot: 9", "yew: 30", "sev: 7"]
m = {}
for l in lines:
    k, v = l.split(": "); m[k] = v
print(f"{len(m)} riddles")
print(f"part 1: root shouts {ev(m, 'root')}")
root = m["root"].split(" ")
left, right = root[0], root[2]
want = ev(m, right) if holds(m, left) else ev(m, left)
side = left if holds(m, left) else right
print(f"the {side} side must reach {want}")
print(f"part 2: you must shout {solve(m, side, want)}")
