import sys, re

def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lines = [l[:-1] if l.endswith("\r") else l for l in lines]
    if len(lines) < 2 or not re.fullmatch(r"[0-9]{1,3}", lines[0]) or int(lines[0]) > 40:
        print("bad input")
        return
    n = int(lines[0])
    s = lines[1]
    rules = []
    for k in range(2, len(lines)):
        line = lines[k]
        if line == "":
            continue
        i = line.find("=>")
        if i <= 0:
            print("bad rule line %d" % (k + 1))
            return
        rules.append((line[:i], line[i + 2:]))

    def pick(cur):
        for lhs, rhs in rules:
            i = cur.find(lhs)
            if i >= 0:
                return i, lhs, rhs
        return None

    print("0: [%s]" % s)
    steps = 0
    while steps < n:
        r = pick(s)
        if r is None:
            break
        i, lhs, rhs = r
        s = s[:i] + rhs + s[i + len(lhs):]
        steps += 1
        if len(s) > 60:
            print("too long at step %d" % steps)
            return
        print("%d: [%s]" % (steps, s))
    if pick(s) is None:
        print("halted after %d steps" % steps)
    else:
        print("step limit %d reached" % n)

main()
