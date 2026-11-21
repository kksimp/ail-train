SMALL = ["a", "an", "the", "and", "or", "of", "in", "on", "to", "for"]
def cap(w): return w[:1].upper() + w[1:].lower()
def hl(t):
    ws = t.split(); out = []
    for i, w in enumerate(ws):
        edge = i == 0 or i == len(ws) - 1
        out.append(w.lower() if w.lower() in SMALL and not edge else cap(w))
    return " ".join(out)
for t in ["the lord OF the rings", "a tale of two cities", "war and peace", "what to look for", "of"]:
    print(hl(t))
