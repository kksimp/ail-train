def settle(gates, x, y):
    wires = {}
    for i in range(3):
        wires[f"x{i}"] = (x >> i) & 1; wires[f"y{i}"] = (y >> i) & 1
    changed = True
    while changed:
        changed = False
        for a, op, b, out in gates:
            if a in wires and b in wires and out not in wires:
                p, q = wires[a], wires[b]
                wires[out] = p & q if op == "AND" else (p | q if op == "OR" else p ^ q)
                changed = True
    return sum(wires.get(f"z{i}", 0) << i for i in range(4))

lines = ["x0 XOR y0 -> z0", "x0 AND y0 -> c0", "x1 XOR y1 -> s1", "s1 XOR c0 -> z1", "x1 OR y1 -> a1", "s1 AND c0 -> b1", "a1 OR b1 -> c1", "x2 XOR y2 -> s2", "s2 XOR c1 -> z2", "x2 AND y2 -> a2", "s2 AND c1 -> b2", "a2 OR b2 -> z3"]
gates = [(w[0], w[1], w[2], w[4]) for w in (l.split(" ") for l in lines)]
print(f"{len(gates)} gates")
print(f"part 1: 5 + 3 gives z = {settle(gates, 5, 3)}")
wrong = []
for x in range(8):
    for y in range(8):
        z = settle(gates, x, y)
        if z != x + y:
            wrong.append(f"{x}+{y}={z}")
print(f"part 2: {len(wrong)} of 64 sums are wrong")
print(f"first wrong sums: {' '.join(wrong[:6])}")
