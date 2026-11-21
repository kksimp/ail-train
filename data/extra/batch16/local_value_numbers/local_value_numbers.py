vn = {}
next_id = [0]

def number_of(name):
    if name in vn:
        return vn[name]
    vn[name] = next_id[0]
    next_id[0] += 1
    return vn[name]

code = [["a", "b", "+", "c"], ["d", "c", "+", "b"], ["e", "b", "-", "c"], ["b", "a", "*", "2"], ["f", "b", "+", "c"], ["g", "c", "-", "b"], ["h", "a", "*", "2"], ["k", "e", "-", "g"]]
holder = {}
exprs = {}
saved = 0
for ins in code:
    x = number_of(ins[1])
    y = number_of(ins[3])
    op = ins[2]
    lo = y if op != "-" and y < x else x
    hi = x if op != "-" and y < x else y
    key = f"{lo}{op}{hi}"
    dst = ins[0]
    if key in exprs and holder.get(exprs[key], "") != "":
        v = exprs[key]
        src = holder[v]
        print(f"{dst} = {src:<4} ; reuses v{v} ({key})")
        vn[dst] = v
        saved += 1
    else:
        v = next_id[0]
        next_id[0] += 1
        exprs[key] = v
        vn[dst] = v
        print(f"{dst} = {ins[1]} {op} {ins[3]} ; v{v}")
    for v2, h in list(holder.items()):
        if h == dst:
            holder[v2] = ""
    holder[vn[dst]] = dst
print(f"{saved} computations replaced by copies")
