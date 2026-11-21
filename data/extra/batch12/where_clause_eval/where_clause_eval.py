nodes = [("cmp", "price", "<", 50), ("cmp", "qty", ">", 0), ("and", 0, 1), ("cmp", "featured", "=", 1), ("or", 2, 3), ("cmp", "discontinued", "=", 1), ("not", 5), ("and", 4, 6)]

def test(i, row):
    n = nodes[i]
    if n[0] == "cmp":
        v = row.get(n[1], 0)
        if n[2] == "<": return v < n[3]
        if n[2] == ">": return v > n[3]
        return v == n[3]
    if n[0] == "and": return test(n[1], row) and test(n[2], row)
    if n[0] == "or": return test(n[1], row) or test(n[2], row)
    return not test(n[1], row)

def text(i):
    n = nodes[i]
    if n[0] == "cmp": return f"{n[1]} {n[2]} {n[3]}"
    if n[0] == "and": return f"({text(n[1])} AND {text(n[2])})"
    if n[0] == "or": return f"({text(n[1])} OR {text(n[2])})"
    return f"NOT {text(n[1])}"

root = len(nodes) - 1
print(f"WHERE {text(root)}")
names = ["lamp", "rug", "vase", "clock", "chair", "mirror"]
rows = [{"price": 35, "qty": 4, "featured": 0, "discontinued": 0}, {"price": 120, "qty": 2, "featured": 1, "discontinued": 0}, {"price": 20, "qty": 0, "featured": 0, "discontinued": 0}, {"price": 45, "qty": 7, "featured": 0, "discontinued": 1}, {"price": 80, "qty": 1, "featured": 0, "discontinued": 0}, {"price": 60, "qty": 3, "featured": 1, "discontinued": 1}]
kept = []
for i, row in enumerate(rows):
    ok = test(root, row)
    print(f"{names[i]:<7} {'keep' if ok else 'skip'}")
    if ok:
        kept.append(names[i])
print(f"{len(kept)} rows: {', '.join(kept)}")
