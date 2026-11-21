import math
text = "we ate ice cream at the beach and the ice cream melted in the sun so we bought more ice cream and sat in the shade of the old pier near the beach and the sun went down over the old pier"
words = text.split(" ")
n = float(len(words))
single = {}
for w in words:
    single[w] = single.get(w, 0) + 1
pairs = {}
for i in range(len(words) - 1):
    k = f"{words[i]} {words[i + 1]}"
    pairs[k] = pairs.get(k, 0) + 1
nb = float(len(words) - 1)
scored = []
for pair, count in pairs.items():
    if count >= 2:
        parts = pair.split(" ")
        pxy = count / nb
        px = single[parts[0]] / n
        py = single[parts[1]] / n
        ratio = pxy / (px * py)
        scored.append((pair, math.log(ratio) / math.log(2.0), count))
ranked = sorted(scored, key=lambda t: -int(t[1] * 1000000.0))
for pair, pmi, count in ranked:
    print(f"{pair:<10} seen {count} times, pmi {pmi:.2f}")
print(f"{len(words)} words, {len(pairs)} different neighbour pairs")
