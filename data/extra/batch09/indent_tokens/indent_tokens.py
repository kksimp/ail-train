def lex(lines):
    stack = [0]
    out = []
    for i, line in enumerate(lines):
        body = line.lstrip(" ")
        if body == "":
            continue
        indent = len(line) - len(body)
        if indent > stack[-1]:
            stack.append(indent)
            out.append("INDENT")
        else:
            while indent < stack[-1]:
                stack.pop()
                out.append("DEDENT")
            if indent != stack[-1]:
                return None, f"line {i + 1}: dedent to {indent} matches no outer level"
        for w in body.split(" "):
            out.append(w)
        out.append("NL")
    while len(stack) > 1:
        stack.pop()
        out.append("DEDENT")
    return out, None

good = ["if ready", "    start engine", "    if fast", "        boost", "", "    stop", "done"]
bad = ["loop", "    step", "  back"]
for prog in [good, bad]:
    toks, err = lex(prog)
    if toks is not None:
        line = []
        for t in toks:
            line.append(t)
            if t == "NL":
                print(" ".join(line))
                line = []
        if line:
            print(" ".join(line))
    else:
        print(f"error: {err}")
