def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

body = [["t1", "n", "*", "4"], ["i", "i", "+", "1"], ["t2", "t1", "+", "base"], ["x", "i", "*", "t2"], ["t3", "k", "+", "1"], ["k", "x", "+", "t3"], ["t4", "t2", "*", "2"], ["s", "s", "+", "t4"]]
defined = {}
for st in body:
    defined[st[0]] = defined.get(st[0], 0) + 1
hoisted = []
moved = set()
changed = True
while changed:
    changed = False
    for i, st in enumerate(body):
        if i in hoisted or defined[st[0]] != 1:
            continue
        ok = True
        for opnd in [st[1], st[3]]:
            inside = opnd in defined
            if not is_number(opnd) and inside and opnd not in moved:
                ok = False
        if ok:
            hoisted.append(i)
            moved.add(st[0])
            changed = True
print("before the loop:")
for i in hoisted:
    st = body[i]
    print(f"    {st[0]} = {st[1]} {st[2]} {st[3]}")
print("loop body:")
for i, st in enumerate(body):
    if i not in hoisted:
        print(f"    {st[0]} = {st[1]} {st[2]} {st[3]}")
print(f"{len(hoisted)} of {len(body)} statements hoisted")
