def jumps(code):
    pair = []
    opn = []
    for i, c in enumerate(code):
        pair.append(-1)
        if c == '[':
            opn.append(i)
        elif c == ']':
            if not opn:
                return None, f"']' at {i} has no '['"
            j = opn.pop()
            pair[i] = j
            pair[j] = i
    if opn:
        return None, f"{len(opn)} '[' never closed"
    return pair, None

def run(src):
    code = src
    pair, err = jumps(code)
    if pair is None:
        return None, err
    cells = [0] * 8
    ptr = 0
    pc = 0
    steps = 0
    out = []
    while pc < len(code):
        c = code[pc]
        steps += 1
        if c == '+':
            cells[ptr] = (cells[ptr] + 1) % 256
        elif c == '-':
            cells[ptr] = (cells[ptr] + 255) % 256
        elif c == '>':
            ptr += 1
        elif c == '<':
            ptr -= 1
        elif c == '.':
            out.append(chr(cells[ptr]))
        elif c == '[':
            if cells[ptr] == 0:
                pc = pair[pc]
        elif c == ']':
            if cells[ptr] != 0:
                pc = pair[pc]
        pc += 1
    return "".join(out) + f" ({steps} steps)", None

programs = [("say Hi", "++++++++[>+++++++++<-]>.+++++++++++++++++++++++++++++++++."), ("2 + 5", "++>+++++[<+>-]++++++++[<++++++>-]<."), ("count to 3", "++++++[>++++++++<-]>+.+.+."), ("broken", "+[>+<-]]"), ("unclosed", "[[+]")]
for name, src in programs:
    text, err = run(src)
    if text is not None:
        print(f"{name:<11} -> {text}")
    else:
        print(f"{name:<11} -> error: {err}")
