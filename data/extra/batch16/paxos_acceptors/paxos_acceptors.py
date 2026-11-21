class Acceptor:
    def __init__(s):
        s.promised, s.acc_n, s.acc_v = 0, 0, "-"

def prepare(accs, n, targets, own):
    best_n = 0
    value = own
    ok = 0
    for t in targets:
        if n > accs[t].promised:
            accs[t].promised = n
            ok += 1
            if accs[t].acc_n > best_n:
                best_n = accs[t].acc_n
                value = accs[t].acc_v
    if ok * 2 <= len(accs):
        return ""
    return value

def accept(accs, n, v, targets):
    ok = 0
    for t in targets:
        if n >= accs[t].promised:
            accs[t].promised = n
            accs[t].acc_n = n
            accs[t].acc_v = v
            ok += 1
    return ok

def rnd(accs, who, n, own, p_to, a_to):
    v = prepare(accs, n, p_to, own)
    if v == "":
        print(f"{who} ballot {n}: no majority of promises")
        return
    note = "its own value" if v == own else "adopted value"
    got = accept(accs, n, v, a_to)
    verdict = "chosen" if got * 2 > len(accs) else "not chosen yet"
    print(f"{who} ballot {n}: proposes {v} ({note}), {got} accepts, {verdict}")

accs = [Acceptor() for i in range(3)]
rnd(accs, "P1", 1, "blue", [0, 1], [0])
rnd(accs, "P2", 2, "green", [0, 1], [0, 1])
rnd(accs, "P1", 1, "red", [2], [2])
rnd(accs, "P3", 3, "gold", [1, 2], [1, 2])
for i, a in enumerate(accs):
    print(f"acceptor {i}: promised {a.promised}, accepted ({a.acc_n}, {a.acc_v})")
