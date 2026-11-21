lines = ["; site settings", "name = Corner Shop", "[server]", "host = 0.0.0.0", "port = 8080", "# old: port = 80", "[database]", "path = data/shop.db", "pool = 4", "pool = 8", "[server]", "debug = false", "broken line here"]
values = {}
sections = []
section = "global"
for i, raw in enumerate(lines):
    line = raw.strip()
    if line == "" or line.startswith(";") or line.startswith("#"):
        continue
    if line.startswith("[") and line.endswith("]"):
        section = line[1:len(line) - 1].strip()
        if section not in sections:
            sections.append(section)
        continue
    at = line.find("=")
    if at < 0:
        print(f"line {i + 1}: no '=' in \"{line}\"")
        continue
    key = f"{section}.{line[:at].strip()}"
    value = line[at + 1:].strip()
    if key in values:
        print(f"line {i + 1}: {key} set again, {values[key]} -> {value}")
    values[key] = value
for s in sections:
    keys = [k for k in values if k.startswith(f"{s}.")]
    print(f"[{s}] {len(keys)} keys")
for k, v in values.items():
    print(f"{k} = {v}")
port = int(values.get("server.port", "0"))
print(f"port + 1 = {port + 1}")
