import sys

data = sys.stdin.read().split("\n")
first = data[0] if data else ""
prog = [c for c in first if c in "<>+-.[]"]
jump = [0] * len(prog)
stack = []
bad = False
for i, c in enumerate(prog):
    if c == "[":
        stack.append(i)
    elif c == "]":
        if not stack:
            bad = True
            break
        j = stack.pop()
        jump[i] = j
        jump[j] = i
if stack:
    bad = True
if bad:
    print("error brackets")
    sys.exit(0)
tape = [0] * 16
ptr = 0
pc = 0
steps = 0
out = []
status = "ok"
while pc < len(prog):
    if steps == 5000:
        status = "limit"
        break
    c = prog[pc]
    steps += 1
    if c == ">":
        if ptr == 15:
            status = "pointer"
            break
        ptr += 1
    elif c == "<":
        if ptr == 0:
            status = "pointer"
            break
        ptr -= 1
    elif c == "+":
        tape[ptr] = (tape[ptr] + 1) % 256
    elif c == "-":
        tape[ptr] = (tape[ptr] - 1) % 256
    elif c == ".":
        out.append(tape[ptr])
    elif c == "[":
        if tape[ptr] == 0:
            pc = jump[pc]
    elif c == "]":
        if tape[ptr] != 0:
            pc = jump[pc]
    pc += 1
print("out:" + "".join(" %d" % v for v in out))
print("%s steps=%d" % (status, steps))
