def as_text(xs):
    return "{" + ", ".join(xs) + "}"

names = ["B0 entry", "B1 test", "B2 body", "B3 exit"]
uses = [[], ["a", "n"], ["b", "c", "a"], ["c"]]
defs = [["a", "b", "n"], ["c"], ["b", "a"], []]
succ = [[1], [2, 3], [1], []]
n = len(names)
live_in = [[] for _ in range(n)]
live_out = [[] for _ in range(n)]
changed = True
rounds = 0
while changed:
    changed = False
    rounds += 1
    for step in range(n):
        b = n - 1 - step
        out = set()
        for s in succ[b]:
            out.update(live_in[s])
        inn = set(uses[b])
        for v in out:
            if v not in defs[b]:
                inn.add(v)
        new_in = sorted(inn)
        new_out = sorted(out)
        if new_in != live_in[b] or new_out != live_out[b]:
            changed = True
            live_in[b] = new_in
            live_out[b] = new_out
for b in range(n):
    print(f"{names[b]:<9} in {as_text(live_in[b])} out {as_text(live_out[b])}")
print(f"fixed point after {rounds} rounds")
