text = "The river ran fast. The river ran cold, and the boats on the river ran with it. Cold water, fast water: the river never rests."
stop = ["the", "and", "on", "with", "it"]
ws = ["".join(c for c in r if c.isalpha() or c == "'") for r in text.lower().split(" ")]
ws = [w for w in ws if w and w not in stop]
c = {}
for w in ws: c[w] = c.get(w, 0) + 1
for w in sorted(c, key=lambda w: (-c[w], w))[:5]: print(f"{w:<7} {c[w]} {'#' * c[w]}")
print(f"{len(ws)} words, {len(c)} different")
