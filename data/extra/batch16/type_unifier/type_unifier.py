pool = []

def mk(name, args):
    pool.append((name[0].islower(), name, args))
    return len(pool) - 1

def resolve(binds, t):
    cur = t
    while pool[cur][0] and pool[cur][1] in binds:
        cur = binds[pool[cur][1]]
    return cur

def show(binds, t):
    term = pool[resolve(binds, t)]
    if not term[2]:
        return term[1]
    return f"{term[1]}[{', '.join(show(binds, a) for a in term[2])}]"

def occurs(binds, v, t):
    term = pool[resolve(binds, t)]
    if term[0]:
        return term[1] == v
    return any(occurs(binds, v, a) for a in term[2])

def unify(binds, a, b):
    ra = resolve(binds, a)
    rb = resolve(binds, b)
    ta = pool[ra]
    tb = pool[rb]
    if ta[0] and tb[0] and ta[1] == tb[1]:
        return ""
    if ta[0]:
        if occurs(binds, ta[1], rb):
            return f"{ta[1]} occurs inside {show(binds, rb)}"
        binds[ta[1]] = rb
        return ""
    if tb[0]:
        return unify(binds, b, a)
    if ta[1] != tb[1] or len(ta[2]) != len(tb[2]):
        return f"{show(binds, ra)} vs {show(binds, rb)}"
    for i in range(len(ta[2])):
        e = unify(binds, ta[2][i], tb[2][i])
        if e != "":
            return e
    return ""

a = mk("a", [])
b = mk("b", [])
int_t = mk("Int", [])
bool_t = mk("Bool", [])
li = mk("List", [int_t])
pairs = [[mk("Fn", [a, int_t]), mk("Fn", [bool_t, b])], [mk("List", [a]), mk("List", [li])], [a, mk("List", [a])], [mk("Pair", [int_t, a]), mk("Pair", [bool_t, int_t])], [mk("Pair", [a, b]), mk("Pair", [b, int_t])]]
for pr in pairs:
    binds = {}
    left = show(binds, pr[0])
    right = show(binds, pr[1])
    err = unify(binds, pr[0], pr[1])
    if err == "":
        got = ", ".join(f"{v} = {show(binds, binds[v])}" for v in sorted(binds))
        print(f"{left} ~ {right}: ok, {got}")
    else:
        print(f"{left} ~ {right}: fails, {err}")
