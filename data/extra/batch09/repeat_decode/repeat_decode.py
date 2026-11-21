def expand(cs, pos):
    out = []
    while pos[0] < len(cs) and cs[pos[0]] != ']':
        c = cs[pos[0]]
        if c.isdigit():
            n = 0
            while cs[pos[0]].isdigit():
                n = n * 10 + int(cs[pos[0]])
                pos[0] += 1
            pos[0] += 1
            inner = expand(cs, pos)
            pos[0] += 1
            out.append(inner * n)
        else:
            out.append(c)
            pos[0] += 1
    return "".join(out)

def decode(s):
    return expand(s, [0])

for s in ["3[ab]2[c]", "2[a3[b]]", "x10[-]y", "2[ab2[cd]]e", "3[z]2[xy]", "plain"]:
    d = decode(s)
    print(f"{s:<12} -> {d} ({len(d)} chars)")
