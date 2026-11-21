def run(ops, write_back):
    lines = []
    mem_writes = 0
    misses = 0
    for t, op in enumerate(ops):
        kind = op[0:1]
        block = int(op[1:])
        at = -1
        for i in range(len(lines)):
            if lines[i][0] == block:
                at = i
        if at < 0:
            misses += 1
            if len(lines) == 3:
                old = 0
                for i in range(3):
                    if lines[i][2] < lines[old][2]:
                        old = i
                if lines[old][1]:
                    mem_writes += 1
                lines.pop(old)
            lines.append([block, False, t])
            at = len(lines) - 1
        lines[at][2] = t
        if kind == "W":
            if write_back:
                lines[at][1] = True
            else:
                mem_writes += 1
    dirty_left = len([l for l in lines if l[1]])
    return [misses, mem_writes, dirty_left]

ops = ["R1", "W1", "W1", "R2", "W2", "W1", "R3", "W3", "R4", "W1", "W1", "W4", "R2", "W2", "W2"]
print(f"ops: {' '.join(ops)}")
a = run(ops, False)
b = run(ops, True)
print(f"write-through: {a[0]} misses, {a[1]} memory writes")
print(f"write-back:    {b[0]} misses, {b[1]} memory writes, {b[2]} dirty lines to flush")
print(f"write-back total after flush: {b[1] + b[2]}")
