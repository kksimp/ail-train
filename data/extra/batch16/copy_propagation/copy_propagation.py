code = [["a", "x"], ["b", "a", "+", "1"], ["c", "a"], ["d", "c", "*", "b"], ["x", "5"], ["e", "a", "+", "c"], ["a", "2"], ["f", "c", "+", "a"], ["g", "b"], ["h", "g", "-", "d"]]
copies = {}
replaced = 0

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for st in code:
    ops = st[1:]
    for k in range(len(ops)):
        if k != 1 or len(ops) == 1:
            if ops[k] in copies:
                ops[k] = copies[ops[k]]
                replaced += 1
    dst = st[0]
    dead = [key for key, src in copies.items() if key == dst or src == dst]
    for key in dead:
        del copies[key]
    is_var = len(ops) == 1 and not is_int(ops[0])
    if is_var and ops[0] != dst:
        copies[dst] = ops[0]
    before = " ".join(st[1:])
    after = " ".join(ops)
    note = "" if before == after else f"   (was {before})"
    print(f"{dst} = {after}{note}")
print(f"{replaced} reads replaced; live copies at the end: {len(copies)}")
