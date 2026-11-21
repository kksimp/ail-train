def value(regs, arg):
    try:
        return int(arg)
    except ValueError:
        return regs.get(arg, 0)

def run(prog, start):
    regs = {"a": start}; out = []; pc = 0
    while 0 <= pc < len(prog):
        w = prog[pc].split(" ")
        op = w[0]
        if op == "cpy": regs[w[1]] = value(regs, w[2])
        elif op == "add": regs[w[1]] = regs.get(w[1], 0) + value(regs, w[2])
        elif op == "mul": regs[w[1]] = regs.get(w[1], 0) * value(regs, w[2])
        elif op == "div": regs[w[1]] = regs.get(w[1], 0) // value(regs, w[2])
        elif op == "mod": regs[w[1]] = regs.get(w[1], 0) % value(regs, w[2])
        elif op == "out": out.append(value(regs, w[1]))
        elif op == "jnz":
            if value(regs, w[1]) != 0:
                pc += value(regs, w[2]) - 1
        pc += 1
    return out

prog = ["cpy b a", "mod b 8", "mul b 3", "add b 1", "mod b 8", "out b", "div a 8", "jnz a -7"]
print(f"{len(prog)} instructions")
print(f"part 1: input 2024 prints {run(prog, 2024)}")
want = [3, 6, 1, 4]
n = 1
while run(prog, n) != want:
    n += 1
print(f"part 2: smallest input printing {want} is {n}")
print(f"check: {n} prints {run(prog, n)}")
