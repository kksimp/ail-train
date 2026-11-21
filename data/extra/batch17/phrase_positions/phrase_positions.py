def build(docs):
    index = {}
    for d, text in enumerate(docs):
        for p, w in enumerate(text.lower().split()):
            index.setdefault(w, []).append([d, p])
    return index

def phrase_docs(index, phrase):
    out = set()
    first = index.get(phrase[0], [])
    for hit in first:
        ok = True
        for k in range(1, len(phrase)):
            want = [hit[0], hit[1] + k]
            if want not in index.get(phrase[k], []):
                ok = False
                break
        if ok:
            out.add(hit[0])
    return out

def near_docs(index, a, b, k):
    out = set()
    for x in index.get(a, []):
        for y in index.get(b, []):
            if x[0] == y[0] and abs(x[1] - y[1]) <= k:
                out.add(x[0])
    return out

docs = ["new york pizza is thin", "pizza in new jersey and york", "york is old and new york is new", "thin crust pizza from new haven"]
index = build(docs)
print(f"{len(index)} distinct words, 'new' at {len(index['new'])} positions")
for q in [["new", "york"], ["york", "pizza"], ["thin", "crust", "pizza"]]:
    hits = sorted(phrase_docs(index, q))
    print(f"\"{' '.join(q)}\" -> docs {hits}")
for a, b, k in [("pizza", "thin", 2), ("pizza", "york", 1), ("new", "pizza", 3)]:
    print(f"{a} NEAR/{k} {b} -> docs {sorted(near_docs(index, a, b, k))}")
