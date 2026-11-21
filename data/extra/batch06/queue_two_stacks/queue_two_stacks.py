i = []; o = []; mv = 0; out = []
for c in "+1 +2 +3 - +4 - - +5 +6 - - - -".split(" "):
    if c == "-":
        if not o:
            while i: o.append(i.pop()); mv += 1
        out.append(str(o.pop()) if o else "empty")
    else: i.append(int(c[1:]))
print(f"dequeued: {' '.join(out)}"); print(f"moves between stacks: {mv}")
