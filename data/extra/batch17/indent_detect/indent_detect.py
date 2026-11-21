def leading(line):
    spaces = 0
    tabs = 0
    for c in line:
        if c == ' ':
            spaces += 1
        elif ord(c) == 9:
            tabs += 1
        else:
            break
    return [spaces, tabs]

def detect(lines):
    steps = {}
    tab_lines = 0
    space_lines = 0
    prev = 0
    for l in lines:
        if l.strip() == "":
            continue
        lead = leading(l)
        if lead[1] > 0:
            tab_lines += 1
        if lead[0] > 0:
            space_lines += 1
        if lead[0] > prev:
            steps[lead[0] - prev] = steps.get(lead[0] - prev, 0) + 1
        prev = lead[0]
    if tab_lines > 0 and space_lines > 0:
        return f"mixed ({tab_lines} tab lines, {space_lines} space lines)"
    if tab_lines > 0:
        return "tabs"
    if len(steps) == 0:
        return "flat"
    best = sorted(steps.keys(), key=lambda k: -steps[k])[0]
    return f"{best} spaces"

t = chr(9)
files = [("a.py", ["def f(x):", "    if x:", "        return 1", "", "    return 2"]), ("b.js", ["function g() {", "  if (a) {", "    b()", "  }", "}"]), ("c.go", ["func h() {", t + "x := 1", t + "if x {", t + t + "y()", t + "}", "}"]), ("d.py", ["class A:", "    def m(self):", t + "pass"]), ("e.txt", ["one", "two"]), ("f.yml", ["a:", "  b:", "      c: 1", "  d: 2", "  e:", "    f: 3"])]
for name, lines in files:
    print(f"{name:<6} {detect(lines)}")
