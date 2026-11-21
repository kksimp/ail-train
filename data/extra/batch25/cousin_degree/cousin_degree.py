def ancestors(p, parent):
    line = [p]
    cur = p
    while cur in parent:
        cur = parent[cur]
        line.append(cur)
    return line

def greats(n):
    if n <= 0:
        return ""
    return "great-" * n

def name(a, b):
    ordinals = ["", "first", "second", "third", "fourth"]
    if a == 0 and b == 0:
        return "same person"
    if a == 0:
        return "parent" if b == 1 else f"{greats(b - 2)}grandparent"
    if b == 0:
        return "child" if a == 1 else f"{greats(a - 2)}grandchild"
    if a == 1 and b == 1:
        return "sibling"
    if a == 1:
        return "aunt or uncle" if b == 2 else f"{greats(b - 3)}grand-aunt or uncle"
    if b == 1:
        return "niece or nephew" if a == 2 else f"{greats(a - 3)}grand-niece or nephew"
    removed = abs(a - b)
    if removed == 0:
        tail = ""
    elif removed == 1:
        tail = " once removed"
    elif removed == 2:
        tail = " twice removed"
    else:
        tail = f" {removed} times removed"
    return f"{ordinals[min(a, b) - 1]} cousin{tail}"

parent = {"Bo": "Al", "Cy": "Al", "Di": "Bo", "Ed": "Cy", "Fay": "Di", "Gus": "Ed", "Hal": "Fay", "Ivo": "Gus", "Jo": "Bo", "Kit": "Hal"}
pairs = [("Di", "Ed"), ("Fay", "Gus"), ("Fay", "Ed"), ("Hal", "Gus"), ("Di", "Jo"), ("Bo", "Gus"), ("Al", "Kit"), ("Kit", "Ivo"), ("Jo", "Hal")]
for x, y in pairs:
    ax = ancestors(x, parent)
    ay = ancestors(y, parent)
    a = -1
    b = -1
    for i, anc in enumerate(ax):
        if a < 0 and anc in ay:
            a = i
            b = ay.index(anc)
    print(f"{y} is {x}'s {name(b, a)} ({a} up, {b} up)")
