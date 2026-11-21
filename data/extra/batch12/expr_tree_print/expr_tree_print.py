def prec(sym):
    return 1 if sym in ("+", "-") else 2

def level(nodes, i):
    n = nodes[i]
    return 3 if n[0] == "num" else prec(n[1])

def text(nodes, i):
    n = nodes[i]
    if n[0] == "num":
        return f"{n[1]}"
    _, sym, l, r = n
    p = prec(sym)
    a = text(nodes, l)
    b = text(nodes, r)
    if level(nodes, l) < p:
        a = f"({a})"
    rl = level(nodes, r)
    if rl < p or (rl == p and sym in ("-", "/")):
        b = f"({b})"
    return f"{a} {sym} {b}"

def ev(nodes, i):
    n = nodes[i]
    if n[0] == "num":
        return n[1]
    _, sym, l, r = n
    a = ev(nodes, l)
    b = ev(nodes, r)
    if sym == "+": return a + b
    if sym == "-": return a - b
    if sym == "*": return a * b
    return int(a / b)

def build(postfix, nodes):
    stack = []
    for tok in postfix.split(" "):
        if tok.lstrip("-").isdigit():
            nodes.append(("num", int(tok)))
        else:
            r = stack.pop()
            l = stack.pop()
            nodes.append(("op", tok, l, r))
        stack.append(len(nodes) - 1)
    return stack.pop()

for pf in ["3 4 + 2 *", "3 4 2 * +", "10 4 2 - -", "10 4 - 2 -", "8 2 / 2 /", "1 2 + 3 4 - *", "6 2 3 * /"]:
    nodes = []
    root = build(pf, nodes)
    print(f"{pf:<16} => {text(nodes, root)} = {ev(nodes, root)}")
