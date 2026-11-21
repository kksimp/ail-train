class Proc:
    def __init__(s, name, stride, p):
        s.name, s.stride, s.p, s.runs = name, stride, p, 0

def pick(ps):
    best = 0
    for i in range(len(ps)):
        if ps[i].p < ps[best].p:
            best = i
    return best

ps = [Proc("A", 10000 // 100, 0), Proc("B", 10000 // 50, 0), Proc("C", 10000 // 25, 0)]
order = []
for slot in range(21):
    if slot == 14:
        low = ps[pick(ps)].p
        ps.append(Proc("D", 10000 // 50, low))
        order.append("|")
    i = pick(ps)
    ps[i].p += ps[i].stride
    ps[i].runs += 1
    order.append(ps[i].name)
print(f"order {''.join(order)}")
for p in ps:
    print(f"{p.name}: stride {p.stride:>3}, pass {p.p:>4}, ran {p.runs} times")
