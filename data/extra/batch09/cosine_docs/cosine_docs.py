import math
def counts(text):
    m = {}
    for w in text.split(" "):
        m[w] = m.get(w, 0) + 1
    return m

def cosine(a, b):
    dot = 0
    for w, k in a.items():
        dot += k * b.get(w, 0)
    na = math.sqrt(float(sum(k * k for k in a.values())))
    nb = math.sqrt(float(sum(k * k for k in b.values())))
    return dot / (na * nb)

notes = ["the train was late again this morning", "late train again so i missed the morning meeting", "bake the bread at a high heat for one hour", "the bread needs one more hour in the oven"]
vs = [counts(t) for t in notes]
for i in range(len(vs)):
    row = [f"{cosine(vs[i], vs[j]):.3f}" for j in range(len(vs))]
    print(f"note {i + 1}: " + "  ".join(row))
best = (0, 1)
best_s = -1.0
for i in range(len(vs)):
    for j in range(i + 1, len(vs)):
        s = cosine(vs[i], vs[j])
        if s > best_s:
            best_s = s
            best = (i, j)
print(f"closest pair: notes {best[0] + 1} and {best[1] + 1}")
