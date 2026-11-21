import math

def bm25(doc, query, docs, avg_len):
    k1 = 1.2
    b = 0.75
    n_docs = float(len(docs))
    score = 0.0
    for term in query:
        cnt = len([d for d in docs if term in d])
        if cnt == 0:
            continue
        n = float(cnt)
        idf = math.log((n_docs - n + 0.5) / (n + 0.5) + 1.0)
        tf = float(len([w for w in doc if w == term]))
        len_norm = 1.0 - b + b * float(len(doc)) / avg_len
        score += idf * tf * (k1 + 1.0) / (tf + k1 * len_norm)
    return score

texts = ["cheap flights to rome and cheap hotels", "rome travel guide with museums and food", "flights flights flights booking", "cheap pasta recipes from rome", "hotel reviews in paris and rome near the museums and parks"]
docs = [t.split() for t in texts]
avg_len = float(sum(len(d) for d in docs)) / float(len(docs))
print(f"average length {avg_len:.1f} words")
for query in [["cheap", "flights"], ["rome", "museums"]]:
    print(f"query: {' '.join(query)}")
    scored = []
    for i, d in enumerate(docs):
        scored.append((i, bm25(d, query, docs, avg_len)))
    ranked = sorted(scored, key=lambda p: -int(math.floor(p[1] * 1000000.0)))
    for p in ranked[:3]:
        print(f"  {p[1]:.3f}  {texts[p[0]]}")
