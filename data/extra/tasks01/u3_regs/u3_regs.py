import sys, re

def toint(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None

def main():
    prog = []
    for k, line in enumerate(sys.stdin.read().split("\n"), 1):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        w = line.split()
        ok = False
        if w[0] in ("inc", "dec") and len(w) == 2 and w[1] in ("a", "b", "c", "d"):
            ok = True
            ins = (w[0], "abcd".index(w[1]), 0)
        elif w[0] == "set" and len(w) == 3 and w[1] in ("a", "b", "c", "d") and toint(w[2]) is not None:
            ok = True
            ins = ("set", "abcd".index(w[1]), toint(w[2]))
        elif w[0] == "jnz" and len(w) == 3 and w[1] in ("a", "b", "c", "d") and re.fullmatch(r"[0-9]+", w[2]):
            ok = True
            ins = ("jnz", "abcd".index(w[1]), int(w[2]))
        elif w[0] == "halt" and len(w) == 1:
            ok = True
            ins = ("halt", 0, 0)
        if not ok:
            print("error line %d" % k)
            return
        prog.append(ins)
    regs = [0, 0, 0, 0]
    pc = 0
    steps = 0
    state = "halted"
    while 0 <= pc < len(prog):
        if steps == 200:
            state = "limit"
            break
        op, r, n = prog[pc]
        steps += 1
        if op == "halt":
            break
        if op == "set":
            regs[r] = n
        elif op == "inc":
            regs[r] += 1
        elif op == "dec":
            regs[r] -= 1
        elif op == "jnz" and regs[r] != 0:
            pc = n
            continue
        pc += 1
    print("%s steps=%d" % (state, steps))
    print("a=%d b=%d c=%d d=%d" % tuple(regs))

main()
