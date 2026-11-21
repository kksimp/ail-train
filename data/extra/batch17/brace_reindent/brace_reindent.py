def brace_delta(line):
    d = 0
    in_str = False
    for c in line:
        if c == '"':
            in_str = not in_str
        elif not in_str and c == '{':
            d += 1
        elif not in_str and c == '}':
            d -= 1
    return d

src = ["int main() {", "int x = 0;", "      if (x > 1) {", 'printf("{ not a brace");', "  while (x < 9) { x++; }", "}", "        else {", "  x = 2;", "    }", "  return x;", "}"]
depth = 0
max_depth = 0
changed = 0
for raw in src:
    line = raw.strip()
    level = depth - 1 if line.startswith("}") else depth
    out = " " * (level * 4) + line
    if out != raw:
        changed += 1
    print(out)
    depth += brace_delta(line)
    max_depth = max(max_depth, depth)
print(f"-- {changed} of {len(src)} lines re-indented, deepest level {max_depth}, final depth {depth}")
