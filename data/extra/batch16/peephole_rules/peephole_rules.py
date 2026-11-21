def pass_once(code):
    out = []
    i = 0
    while i < len(code):
        cur = code[i]
        nxt = code[i + 1] if i + 1 < len(code) else ""
        w = cur.split(" ")
        arg = w[1] if len(w) > 1 else ""
        if cur == "add 0" or cur == "mul 1":
            i += 1
        elif w[0] == "push" and nxt == f"pop {arg}":
            i += 2
        elif w[0] == "store" and nxt == f"load {arg}":
            out.append(cur)
            i += 2
        elif w[0] == "jmp" and nxt == f"{arg}:":
            i += 1
        else:
            out.append(cur)
            i += 1
    return out

code = ["load x", "add 0", "store y", "load y", "push r1", "mul 1", "pop r1", "jmp L1", "L1:", "push r2", "pop r3", "mul 1", "add 5", "jmp L2", "store z", "L2:", "ret"]
print(f"start: {len(code)} instructions")
p = 1
while True:
    next_code = pass_once(code)
    if len(next_code) == len(code):
        break
    print(f"pass {p}: {len(code)} -> {len(next_code)}")
    code = next_code
    p += 1
for line in code:
    print(f"    {line}")
