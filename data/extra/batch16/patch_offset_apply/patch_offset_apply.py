def matches(lines, start, old):
    if start < 0 or start + len(old) > len(lines):
        return False
    return all(lines[start + k] == old[k] for k in range(len(old)))

def signed(n):
    return f"+{n}" if n > 0 else f"{n}"

lines = ["# settings", "name = demo", "#", "[server]", "host = a", "port = 80", "#", "[db]", "user = app", "pool = 5", "retry = 1"]
hunks = [(3, ["[server]", "host = a"], ["[server]", "host = b", "tls = on"]), (8, ["user = app", "pool = 5"], ["user = app", "pool = 20"]), (2, ["[cache]", "size = 1"], ["[cache]", "size = 2"])]
delta = 0
for at, old, new in hunks:
    guess = at - 1 + delta
    placed = -1
    for dist in range(4):
        for sign in [1, -1]:
            if placed < 0 and matches(lines, guess + sign * dist, old):
                placed = guess + sign * dist
    if placed < 0:
        print(f"hunk at line {at}: rejected, text not found")
        continue
    lines = lines[:placed] + new + lines[placed + len(old):]
    print(f"hunk at line {at}: applied at line {placed + 1} (offset {signed(placed - guess)})")
    delta += len(new) - len(old)
for i, l in enumerate(lines):
    print(f"{i + 1:>2} {l}")
