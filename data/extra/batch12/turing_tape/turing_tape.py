def run(rules, inp, start):
    tape = {}
    for i, ch in enumerate(inp):
        tape[i] = ch
    head = len(inp) - 1 if len(inp) > 0 else 0
    if start == "bb_a":
        head = 0
    state = start
    steps = 0
    while state != "halt" and steps < 100:
        sym = tape.get(head, '_')
        key = f"{state}:{sym}"
        if key not in rules:
            break
        w, mv, nxt = rules[key]
        tape[head] = w
        head += mv
        state = nxt
        steps += 1
    ks = sorted(tape.keys())
    cells = [tape.get(i, '_') for i in range(ks[0], ks[-1] + 1)]
    return ["".join(cells), f"{steps}"]

inc = {"inc:1": ('0', -1, "inc"), "inc:0": ('1', 0, "halt"), "inc:_": ('1', 0, "halt")}
for n in ["1011", "111", "0", "1001"]:
    r = run(inc, n, "inc")
    print(f"increment {n}: {r[0]} in {r[1]} steps")
bb = {"bb_a:_": ('1', 1, "bb_b"), "bb_a:1": ('1', -1, "bb_b"), "bb_b:_": ('1', -1, "bb_a"), "bb_b:1": ('1', 1, "halt")}
r = run(bb, "", "bb_a")
print(f"busy beaver: tape {r[0]} after {r[1]} steps")
