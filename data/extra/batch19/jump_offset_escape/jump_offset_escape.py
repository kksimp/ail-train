def escape(start, strange):
    jumps = list(start); pc = 0; steps = 0
    while 0 <= pc < len(jumps):
        off = jumps[pc]
        jumps[pc] += -1 if strange and off >= 3 else 1
        pc += off; steps += 1
    return steps

offsets = [0, 3, 0, 1, -3, 2, -1, 4, -6, 1]
print(f"offsets: {offsets}")
print(f"part 1: out after {escape(offsets, False)} jumps")
print(f"part 2: out after {escape(offsets, True)} jumps")
