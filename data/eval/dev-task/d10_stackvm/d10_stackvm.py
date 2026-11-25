import re
import sys

stack = []
n = 0
for line in sys.stdin.read().splitlines():
    n += 1
    w = line.split()
    if not w:
        continue
    op = w[0]
    need = {"push": 0, "dup": 1, "pop": 1, "print": 1, "add": 2, "sub": 2, "mul": 2, "swap": 2}
    msg = ""
    if op not in need or (op != "push" and len(w) != 1):
        msg = "unknown instruction"
    elif op == "push":
        if len(w) != 2 or not re.fullmatch(r"-?[0-9]+", w[1]):
            msg = "bad operand"
        else:
            stack.append(int(w[1]))
    elif len(stack) < need[op]:
        msg = "stack underflow"
    elif op == "dup":
        stack.append(stack[-1])
    elif op == "pop":
        stack.pop()
    elif op == "print":
        print(stack[-1])
    elif op == "swap":
        stack[-1], stack[-2] = stack[-2], stack[-1]
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b if op == "add" else a - b if op == "sub" else a * b)
    if msg:
        print("error: line %d: %s" % (n, msg))
        sys.exit(0)
print("stack: " + (" ".join(map(str, stack)) if stack else "empty"))
