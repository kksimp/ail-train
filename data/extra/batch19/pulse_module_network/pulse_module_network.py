def build(lines):
    net = {"kinds": {}, "outs": {}, "on": {}, "memory": {}, "lows": 0, "highs": 0}
    for l in lines:
        a, b = l.split(" -> ")
        name = a; first = a[0]
        if first in "%&":
            name = a[1:]
        net["kinds"][name] = first
        net["outs"][name] = b.split(", ")
    for name, targets in net["outs"].items():
        for t in targets:
            if net["kinds"].get(t, ' ') == '&':
                net["memory"][f"{t}<{name}"] = False
            if net["kinds"].get(t, ' ') == '%':
                net["on"][t] = False
    return net

def press(net):
    queue = [("button", "broadcaster", False)]; head = 0
    kinds, outs, on, memory = net["kinds"], net["outs"], net["on"], net["memory"]
    while head < len(queue):
        frm, to, high = queue[head]; head += 1
        if high: net["highs"] += 1
        else: net["lows"] += 1
        if to not in kinds:
            continue
        send = high
        k = kinds[to]
        if k == '%':
            if high:
                continue
            on[to] = not on.get(to, False)
            send = on[to]
        elif k == '&':
            memory[f"{to}<{frm}"] = high
            send = not all(memory[x] for x in memory if x.startswith(f"{to}<"))
        for o in outs[to]:
            queue.append((to, o, send))

def state(net):
    flips = "".join("1" if net["on"][k] else "0" for k in sorted(net["on"]))
    mems = "".join("1" if net["memory"][k] else "0" for k in sorted(net["memory"]))
    return f"{flips}|{mems}"

lines = ["broadcaster -> fa", "%fa -> fb, gate", "%fb -> fc, gate", "%fc -> gate", "&gate -> lamp"]
net = build(lines)
start = state(net)
for _ in range(1000):
    press(net)
print(f"after 1000 presses: {net['lows']} low and {net['highs']} high pulses")
print(f"part 1: product {net['lows'] * net['highs']}")
again = build(lines); presses = 0
while presses == 0 or state(again) != start:
    press(again); presses += 1
    if presses > 5000:
        break
print(f"part 2: the network is back to its start state after {presses} presses")
