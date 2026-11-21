def pretty(src):
    lines = []
    cur = []
    depth = 0
    in_str = False
    escaped = False
    for c in src:
        if in_str:
            cur.append(c)
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
            cur.append(c)
        elif c == '{' or c == '[':
            cur.append(c)
            lines.append("".join(cur))
            depth += 1
            cur = ["  " * depth]
        elif c == '}' or c == ']':
            lines.append("".join(cur))
            depth -= 1
            cur = ["  " * depth, c]
        elif c == ',':
            cur.append(",")
            lines.append("".join(cur))
            cur = ["  " * depth]
        elif c == ':':
            cur.append(": ")
        elif c != ' ':
            cur.append(c)
    lines.append("".join(cur))
    return [l for l in lines if l.strip() != ""]

def minify(lines):
    out = []
    in_str = False
    escaped = False
    for c in "\n".join(lines):
        if in_str:
            out.append(c)
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
            out.append(c)
        elif c != ' ' and c != '\n':
            out.append(c)
    return "".join(out)

src = '{"name":"Ana, \\"the boss\\"","tags":["a","b: c"],"age":34,"pets":[],"home":{"city":"Oslo","zip":false}}'
lines = pretty(src)
for l in lines:
    print(l)
back = minify(lines)
eq = "true" if back == src else "false"
print(f"round trip equal: {eq}, {len(src)} chars -> {len(lines)} lines")
