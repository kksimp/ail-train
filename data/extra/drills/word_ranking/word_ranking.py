def count_words(text):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts

def top(counts, n):
    return sorted(counts, key=lambda k: -counts[k])[:max(n, 0)]

counts = count_words("the cat and the dog and the bird saw the cat")
print(len(counts))
for w in top(counts, 3):
    print(f"{w}: {counts[w]}")
total = sum(counts.values())
pct = {k: v * 100 // total for k, v in counts.items()}
for w in sorted(pct):
    print(f"{w:<5}{pct[w]:>3}%")
print(len(top(counts, 0)))
print(len(top(counts, 99)))
print(max(counts.values()))
print(",".join(k for k, v in counts.items() if v == 1))
