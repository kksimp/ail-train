def group_of(word, groups):
    for g in groups:
        if word in g:
            return g
    return [word]

def score(doc, query, groups):
    total = 0
    for q in query:
        if q in doc:
            total += 2
        elif any(s in doc for s in group_of(q, groups)):
            total += 1
        else:
            return 0
    return total

groups = [["couch", "sofa", "settee"], ["cheap", "budget", "affordable"], ["tv", "television"], ["stand", "table", "unit"]]
docs = ["affordable grey sofa with storage", "leather couch three seater", "budget tv stand oak", "cheap couch cover", "television unit with drawers", "glass coffee table"]
for query in [["cheap", "couch"], ["tv", "stand"], ["sofa"]]:
    print(f"query: {' '.join(query)}")
    hits = []
    for d in docs:
        s = score(d.split(), query, groups)
        if s > 0:
            hits.append((s, d))
    for h in sorted(hits, key=lambda p: -p[0]):
        print(f"  {h[0]}  {h[1]}")
