def lookup(table, name):
    for e in reversed(table):
        if e[0] == name:
            return e
    return None

script = ["let x", "let y", "enter", "use x", "let x", "use x", "enter", "let z", "use y", "use x", "let z", "leave", "use z", "leave", "use x", "use w"]
table = []
depth = 0
for i, cmd in enumerate(script):
    ln = i + 1
    w = cmd.split(" ")
    if w[0] == "enter":
        depth += 1
    elif w[0] == "leave":
        table = [e for e in table if e[1] < depth]
        depth -= 1
    elif w[0] == "let":
        prev = lookup(table, w[1])
        if prev is not None:
            if prev[1] == depth:
                print(f"line {ln:>2}: {w[1]} declared twice in one block (first at line {prev[2]})")
                continue
            print(f"line {ln:>2}: {w[1]} shadows the one from line {prev[2]}")
        table.append((w[1], depth, ln))
    else:
        e = lookup(table, w[1])
        if e is not None:
            print(f"line {ln:>2}: {w[1]} -> line {e[2]}, {depth - e[1]} blocks out")
        else:
            print(f"line {ln:>2}: {w[1]} is not declared")
print(f"names left at top level: {len(table)}")
