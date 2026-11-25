import sys, re

IDENT = re.compile(r"[a-z_][a-z0-9_]*")
NUM = re.compile(r"-?[0-9]{1,6}")
MEMOPS = ("STORE", "LOADM", "ADDM", "SUBM", "MULM")
NUMOPS = ("LOAD", "ADD", "SUB", "MUL")
JOPS = ("JMP", "JZ", "JNEG")

def main():
    prog = []
    labels = {}
    for k, raw in enumerate(sys.stdin.read().split("\n"), 1):
        line = raw.strip()
        if line == "" or line.startswith("#"):
            continue
        if line.endswith(":"):
            name = line[:-1]
            if IDENT.fullmatch(name) and name not in labels:
                labels[name] = len(prog)
                continue
            print("error line %d" % k)
            return
        w = line.split(" ")
        op = w[0]
        if op in ("PRINT", "HALT") and len(w) == 1:
            prog.append((op, 0, ""))
        elif op in NUMOPS and len(w) == 2 and NUM.fullmatch(w[1]):
            prog.append((op, int(w[1]), ""))
        elif op in MEMOPS and len(w) == 2 and re.fullmatch(r"[0-9]", w[1]):
            prog.append((op, int(w[1]), ""))
        elif op in JOPS and len(w) == 2 and IDENT.fullmatch(w[1]):
            prog.append((op, 0, w[1]))
        else:
            print("error line %d" % k)
            return
    for op, n, lab in prog:
        if op in JOPS and lab not in labels:
            print("error label " + lab)
            return
    acc = 0
    mem = [0] * 10
    pc = 0
    steps = 0
    out = []
    final = None
    while pc < len(prog):
        if steps == 1000:
            final = "limit acc=%d steps=%d" % (acc, steps)
            break
        op, n, lab = prog[pc]
        steps += 1
        pc += 1
        if op == "HALT":
            break
        if op == "PRINT":
            out.append(str(acc))
        elif op == "LOAD":
            acc = n
        elif op == "STORE":
            mem[n] = acc
        elif op == "LOADM":
            acc = mem[n]
        elif op == "JMP":
            pc = labels[lab]
        elif op == "JZ":
            if acc == 0:
                pc = labels[lab]
        elif op == "JNEG":
            if acc < 0:
                pc = labels[lab]
        else:
            v = n if op in NUMOPS else mem[n]
            if op in ("ADD", "ADDM"):
                acc += v
            elif op in ("SUB", "SUBM"):
                acc -= v
            else:
                acc *= v
            if abs(acc) > 1000000000:
                final = "error overflow steps=%d" % steps
                break
    if final is None:
        final = "acc=%d steps=%d" % (acc, steps)
    for v in out:
        print(v)
    print(final)

main()
