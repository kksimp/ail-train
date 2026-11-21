def merge_word(syms, a, b):
    out = []
    i = 0
    while i < len(syms):
        if i + 1 < len(syms) and syms[i] == a and syms[i + 1] == b:
            out.append(a + b)
            i += 2
        else:
            out.append(syms[i])
            i += 1
    return out

corpus = [("low", 5), ("lower", 2), ("newest", 6), ("widest", 3), ("lowest", 2)]
words = [list(c[0]) for c in corpus]
counts = [c[1] for c in corpus]
merges = []
for step in range(1, 7):
    pairs = {}
    for wi, syms in enumerate(words):
        for i in range(len(syms) - 1):
            k = f"{syms[i]} {syms[i + 1]}"
            pairs[k] = pairs.get(k, 0) + counts[wi]
    best = ""
    best_n = 0
    for key in sorted(pairs):
        if pairs[key] > best_n:
            best = key
            best_n = pairs[key]
    ab = best.split(" ")
    merges.append(ab)
    for wi in range(len(words)):
        words[wi] = merge_word(words[wi], ab[0], ab[1])
    print(f"merge {step}: {ab[0]} + {ab[1]} ({best_n} times)")
for wi, syms in enumerate(words):
    print(f"{corpus[wi][0]:<7} " + " ".join(syms))
fresh = list("slowest")
for m in merges:
    fresh = merge_word(fresh, m[0], m[1])
print("slowest -> " + " ".join(fresh))
