def report(name, lines):
    h = 0
    for l in lines:
        if "ERROR" in l: break
        h += 1
    print(f"{name}: {h} of {len(lines)} lines before any error")
    bad = next((l for l in lines if "ERROR" in l), None)
    if bad: print(f"  first error: {bad}")
    i = 0
    while i < len(lines) and "login:" not in lines[i]: i += 1
    users = [l.split(" ")[-1] for l in lines[i + 1:]]
    if not users: print("  nobody signed in")
    else: print(f"  signed in: {', '.join(users)}")
report("monday boot", ["[0.00] kernel start", "[0.41] mount root", "[1.02] net up", "[1.30] ERROR disk sdb missing", "[1.31] retry sdb", "[2.10] login: ready", "[2.50] user anna", "[3.00] user ben"])
report("tuesday boot", ["[0.00] kernel start", "[0.39] mount root", "[0.97] net up", "[1.88] login: ready"])
