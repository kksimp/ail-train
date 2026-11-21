def parse_level(t, pos, env, level):
    if level == 2:
        return parse_not(t, pos, env)
    op = "or" if level == 0 else "and"
    v = parse_level(t, pos, env, level + 1)
    while pos[0] < len(t) and t[pos[0]] == op:
        pos[0] += 1
        r = parse_level(t, pos, env, level + 1)
        v = (v or r) if level == 0 else (v and r)
    return v

def parse_not(t, pos, env):
    tok = t[pos[0]]
    pos[0] += 1
    if tok == "not":
        return not parse_not(t, pos, env)
    if tok == "(":
        v = parse_level(t, pos, env, 0)
        pos[0] += 1
        return v
    return env.get(tok, False)

def table(formula):
    t = [w for w in formula.replace("(", " ( ").replace(")", " ) ").split(" ") if w != ""]
    names = sorted(set(w for w in t if len(w) == 1 and w != "(" and w != ")"))
    n = len(names)
    out = []
    for row in range(1 << n):
        env = {}
        for k, name in enumerate(names):
            env[name] = ((row >> (n - 1 - k)) & 1) == 1
        out.append(parse_level(t, [0], env, 0))
    return out

f = "(a or b) and not c"
print(f"a b c | {f}")
rows = table(f)
for row in range(8):
    cells = " ".join(str(x) for x in [(row >> 2) & 1, (row >> 1) & 1, row & 1])
    r = 1 if rows[row] else 0
    print(f"{cells} | {r}")
for g in ["a or not a", "a and not a", "(a and b) or (not a and not b)"]:
    vs = table(g)
    trues = sum(1 for x in vs if x)
    verdict = "tautology" if trues == len(vs) else ("contradiction" if trues == 0 else "satisfiable")
    print(f"{g}: true in {trues} of {len(vs)} rows, {verdict}")
