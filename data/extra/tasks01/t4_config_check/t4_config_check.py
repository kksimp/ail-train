import sys


def digits(v):
    return v != "" and all("0" <= c <= "9" for c in v)


def valid(k, v):
    if k == "host":
        return v != "" and " " not in v
    if k == "port":
        return digits(v) and 1 <= int(v) <= 65535
    if k == "workers":
        return digits(v) and 1 <= int(v) <= 64
    if k == "debug":
        return v in ("true", "false")
    if k == "mode":
        return v in ("dev", "test", "prod")
    return False


KNOWN = ("host", "port", "workers", "debug", "mode")
problems = []
seen = set()
for n, raw in enumerate(sys.stdin.read().split("\n"), 1):
    line = raw.strip(" \t\r")
    if line == "" or line.startswith("#"):
        continue
    if "=" not in line:
        problems.append(f"line {n}: missing '='")
        continue
    k, v = line.split("=", 1)
    k, v = k.strip(), v.strip()
    if k == "":
        problems.append(f"line {n}: empty key")
    elif k not in KNOWN:
        problems.append(f"line {n}: unknown key '{k}'")
    elif k in seen:
        problems.append(f"line {n}: duplicate key '{k}'")
    elif not valid(k, v):
        problems.append(f"line {n}: bad value for '{k}': '{v}'")
    else:
        seen.add(k)
for k in ("host", "port"):
    if k not in seen:
        problems.append(f"missing required key '{k}'")
for p in problems:
    print(p)
print("ok" if not problems else f"errors: {len(problems)}")
