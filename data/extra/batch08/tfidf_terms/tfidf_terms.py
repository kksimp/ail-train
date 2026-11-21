import math
docs = ["the cat sat on the mat", "the dog chased the cat", "a dog and a cat played in the park", "rain fell on the park all day"]
df = {}
for d in docs:
    for w in set(d.split()): df[w] = df.get(w, 0) + 1
for i, d in enumerate(docs):
    ws = d.split(); c = {}
    for w in ws: c[w] = c.get(w, 0) + 1
    picks = []; taken = set()
    for rnd in range(2):
        best = ""; bs = -1.0
        for w in sorted(c):
            if w not in taken:
                s = c[w] / len(ws) * math.log(len(docs) / df[w])
                if s > bs: best = w; bs = s
        taken.add(best); picks.append(f"{best} {bs:.3f}")
    print(f"note {i + 1}: {', '.join(picks)}")
