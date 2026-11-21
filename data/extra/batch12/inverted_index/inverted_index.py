def both(a, b):
    i = 0; j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i]); i += 1; j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out

def either(a, b):
    return sorted(set(a) | set(b))

notes = ["printer jams on floor two", "wifi drops in meeting room", "printer out of toner", "laptop wifi slow on floor two", "meeting room screen broken", "toner ordered for printer", "laptop battery swollen"]
index = {}
for i, n in enumerate(notes):
    for w in n.split():
        post = index.get(w, [])
        if i not in post:
            index.setdefault(w, []).append(i)
print(f"{len(index)} words indexed")
queries = [["printer", "AND", "toner"], ["wifi", "OR", "laptop"], ["floor", "AND", "wifi"], ["printer", "NOT", "toner"], ["room", "AND", "fax"]]
for q in queries:
    a = index.get(q[0], [])
    b = index.get(q[2], [])
    if q[1] == "AND":
        hits = both(a, b)
    elif q[1] == "OR":
        hits = either(a, b)
    else:
        hits = [x for x in a if x not in b]
    print(f"{' '.join(q)}: notes {hits}")
