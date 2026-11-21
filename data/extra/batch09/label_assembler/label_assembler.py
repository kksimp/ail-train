def opcodes():
    return {"HALT": 0, "LOAD": 1, "SUB": 3, "OUT": 4, "JZ": 5, "JMP": 6}

def assemble(src):
    ops = opcodes()
    labels = {}
    code = []
    for line in src:
        ws = line.split(";")[0].split()
        if ws and ws[0].endswith(":"):
            labels[ws[0][:-1]] = len(code)
            ws = ws[1:]
        if ws:
            code.append(ws)
    out = []
    for ws in code:
        if ws[0] not in ops:
            return None, f"unknown instruction {ws[0]}"
        op = ops[ws[0]]
        arg = 0
        if len(ws) > 1:
            if ws[1].lstrip("-").isdigit():
                arg = int(ws[1])
            elif ws[1] in labels:
                arg = labels[ws[1]]
            else:
                return None, f"unknown label {ws[1]}"
        out.append(op * 100 + arg)
    return out, None

def run(words):
    acc = 0
    pc = 0
    outputs = []
    while pc < len(words):
        op = words[pc] // 100
        arg = words[pc] % 100
        pc += 1
        if op == 1:
            acc = arg
        elif op == 3:
            acc -= arg
        elif op == 4:
            outputs.append(acc)
        elif op == 6 or (op == 5 and acc == 0):
            pc = arg
        elif op == 0:
            break
    return outputs

countdown = ["start: LOAD 4", "loop:  OUT        ; show the counter", "       SUB 1", "       JZ done", "       JMP loop", "done:  LOAD 99", "       OUT", "       HALT"]
words, err = assemble(countdown)
if words is not None:
    for i, w in enumerate(words):
        print(f"{i:02}  {w:03}  {countdown[i].strip()}")
    print(f"output: {run(words)}")
else:
    print(f"error: {err}")
