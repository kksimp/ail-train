lines = ["app:", "  name: shop", "  server:", "    host: 0.0.0.0", "    port: 8080", "  cache:", "    size: 64", "db:", "  path: data.db", "   pool: 4", "  user: admin", "logging: off"]
stack = []
count = 0
for i, line in enumerate(lines):
    trimmed = line.lstrip(" ")
    indent = len(line) - len(trimmed)
    if indent % 2 != 0 or indent // 2 > len(stack):
        print(f"line {i + 1}: bad indent of {indent} spaces")
        continue
    while len(stack) > indent // 2:
        stack.pop()
    parts = trimmed.split(":", 1)
    key = parts[0].strip()
    value = parts[1].strip()
    if value == "":
        stack.append(key)
    else:
        prefix = ".".join(stack)
        path = key if prefix == "" else f"{prefix}.{key}"
        print(f"{path} = {value}")
        count += 1
print(f"{count} values read")
