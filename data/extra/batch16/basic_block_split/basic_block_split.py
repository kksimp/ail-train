def label_of(line):
    if line.startswith("L") and ":" in line:
        return line.split(":")[0]
    return ""

code = ["i = 0", "s = 0", "L1: if i >= n goto L4", "t = i % 2", "if t == 0 goto L2", "s = s + i", "goto L3", "L2: s = s - i", "L3: i = i + 1", "goto L1", "L4: return s"]
n = len(code)
leader = [False] * n
leader[0] = True
for i in range(n):
    if label_of(code[i]) != "":
        leader[i] = True
    if "goto" in code[i] and i + 1 < n:
        leader[i + 1] = True
starts = []
owner = {}
for i in range(n):
    if leader[i]:
        starts.append(i)
    lab = label_of(code[i])
    if lab != "":
        owner[lab] = len(starts) - 1
for b in range(len(starts)):
    stop = starts[b + 1] if b + 1 < len(starts) else n
    last = code[stop - 1]
    words = last.split(" ")
    succ = []
    if "goto" in last:
        succ.append(f"B{owner[words[-1]]}")
    uncond = "goto" in last and "if " not in last
    if not uncond and "return" not in last and b + 1 < len(starts):
        succ.append(f"B{b + 1}")
    targets = "none" if not succ else ", ".join(succ)
    print(f"B{b}: lines {starts[b]}-{stop - 1} ({stop - starts[b]} instr), next: {targets}")
print(f"{len(starts)} blocks from {n} instructions")
