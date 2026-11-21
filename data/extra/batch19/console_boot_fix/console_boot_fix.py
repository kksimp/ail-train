def run(prog, flip):
    acc = 0; pc = 0; seen = set()
    while pc < len(prog):
        if pc in seen:
            return [0, acc]
        seen.add(pc)
        op, n = prog[pc].split(" "); n = int(n)
        if pc == flip:
            op = "nop" if op == "jmp" else ("jmp" if op == "nop" else op)
        if op == "acc":
            acc += n; pc += 1
        elif op == "jmp":
            pc += n
        else:
            pc += 1
    return [1, acc]

prog = ["nop +2", "acc +5", "jmp +3", "acc -2", "jmp -3", "acc +4", "jmp -5", "acc +10", "nop -1", "acc +1"]
print(f"{len(prog)} lines, {sum(1 for l in prog if l.startswith('jmp'))} jumps")
print(f"part 1: accumulator {run(prog, -1)[1]} before the loop repeats")
for i in range(len(prog)):
    if prog[i].startswith("acc"): continue
    r = run(prog, i)
    if r[0] == 1:
        print(f"part 2: flipping line {i} ({prog[i]}) ends with accumulator {r[1]}")
        break
