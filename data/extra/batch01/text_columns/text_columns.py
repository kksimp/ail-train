def transpose(rows):
    w = max(len(r) for r in rows)
    return [[r[c] if c < len(r) else "-" for r in rows] for c in range(w)]
def render(rows):
    cols = max(len(r) for r in rows)
    widths = [max(len(r[c]) if c < len(r) else 0 for r in rows) for c in range(cols)]
    return [" | ".join(r[i].ljust(widths[i]) for i in range(len(r))).rstrip() for r in rows]
rows = [["name", "role", "team"], ["Mira", "lead"], ["Joaquin", "dev", "core", "x"], ["Li", "qa", "web"]]
for l in render(rows):
    print(l)
print("")
t = transpose(rows)
for l in render(t):
    print(l)
print(f"{len(t)} x {len(t[0])}")
