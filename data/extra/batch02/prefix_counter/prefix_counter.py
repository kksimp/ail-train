words = ["car", "card", "care", "careful", "cart", "cat", "dog", "dot", "door", "card"]
c = {}
for w in words:
    for i in range(1, len(w) + 1):
        c[w[:i]] = c.get(w[:i], 0) + 1
for q in ["ca", "car", "care", "do", "x", "cards"]:
    print(f"{q}: {c.get(q, 0)}")
u = {}
for w in words: u[w] = u.get(w, 0) + 1
for q in ["car", "do"]:
    m = sorted([w for w in u if w.startswith(q)], key=lambda w: (-u[w], w))[:3]
    print(f"complete '{q}': {', '.join(m)}")
