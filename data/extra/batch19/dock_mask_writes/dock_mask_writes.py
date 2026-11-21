def apply_value(mask, v):
    out = v
    for i, ch in enumerate(mask):
        bit = 1 << (7 - i)
        if ch == '1': out |= bit
        elif ch == '0': out &= 255 - bit
    return out

def addresses(mask, addr):
    outs = [0]
    for i, ch in enumerate(mask):
        bit = 1 << (7 - i)
        nxt = []
        for a in outs:
            if ch == 'X':
                nxt.append(a); nxt.append(a | bit)
            elif ch == '1' or (addr & bit) != 0:
                nxt.append(a | bit)
            else:
                nxt.append(a)
        outs = nxt
    return outs

prog = ["mask = 1X0X01X0", "mem[3] = 77", "mem[40] = 5", "mask = X10000X1", "mem[3] = 200", "mem[9] = 18"]
mask = ""; mem1 = {}; mem2 = {}
for line in prog:
    k, v = line.split(" = ")
    if k == "mask":
        mask = v; continue
    addr = int(k[4:-1]); v = int(v)
    mem1[addr] = apply_value(mask, v)
    for a in addresses(mask, addr):
        mem2[a] = v
shown = " ".join(f"{k}={v}" for k, v in mem1.items())
print(f"memory after part 1 rules: {shown}")
print(f"part 1: sum {sum(mem1.values())}")
print(f"part 2: {len(mem2)} addresses written, sum {sum(mem2.values())}")
