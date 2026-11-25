import re, sys
from math import gcd

def norm(n, d):
    g = gcd(abs(n), d)
    return n // g, d // g

def parse_operand(t):
    m = re.fullmatch(r"(-?)([0-9]{1,2})(?:/([0-9]{1,2}))?", t)
    if not m:
        return None
    n = int(m.group(2)) * (-1 if m.group(1) else 1)
    d = int(m.group(3)) if m.group(3) is not None else 1
    return n, d

def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    count = 0
    for k, raw in enumerate(lines, 1):
        toks = raw.split()
        if not toks:
            continue
        err = None
        operands = []
        ops = []
        for i, t in enumerate(toks):
            if i % 2 == 0:
                o = parse_operand(t)
                if o is None:
                    err = "bad expression"
                    break
                if o[1] == 0:
                    err = "zero denominator"
                    break
                operands.append(o)
            else:
                if t not in ("+", "-", "*", "/"):
                    err = "bad expression"
                    break
                ops.append(t)
        if err is None and (len(toks) % 2 == 0 or len(operands) > 4):
            err = "bad expression"
        if err is None:
            n, d = norm(*operands[0])
            for op, (a, b) in zip(ops, operands[1:]):
                if op == "+":
                    n, d = norm(n * b + a * d, d * b)
                elif op == "-":
                    n, d = norm(n * b - a * d, d * b)
                elif op == "*":
                    n, d = norm(n * a, d * b)
                else:
                    if a == 0:
                        err = "zero denominator"
                        break
                    n, d = n * b, d * a
                    if d < 0:
                        n, d = -n, -d
                    n, d = norm(n, d)
        if err:
            print(f"line {k}: {err}")
        else:
            print(f"{n}" if d == 1 else f"{n}/{d}")
            count += 1
    print(f"evaluated {count}")

main()
