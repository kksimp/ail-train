def strip(s, esc):
    cs = list(s)
    text = []
    codes = []
    i = 0
    while i < len(cs):
        if cs[i] == esc and i + 1 < len(cs) and cs[i + 1] == '[':
            j = i + 2
            code = []
            while j < len(cs) and not cs[j].isalpha():
                code.append(cs[j])
                j += 1
            codes.append("".join(code))
            i = j + 1
        else:
            text.append(cs[i])
            i += 1
    return ["".join(text), " ".join(codes)]

esc = chr(27)
red = esc + "[31m"
bold = esc + "[1;32m"
off = esc + "[0m"
lines = [red + "FAIL" + off + " parser", bold + "PASS" + off + " lexer", "plain line", red + esc + "[4mWARN" + off + " slow test " + bold + "(2.1s)" + off]
widest = 0
for line in lines:
    parts = strip(line, esc)
    visible = parts[0]
    widest = max(widest, len(visible))
    print(f"{visible:<26} raw {len(line):>2}, visible {len(visible):>2}, codes [{parts[1]}]")
print(f"column width needed: {widest}")
