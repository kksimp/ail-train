def wo(s): return set(s.lower().split(" "))
def ja(a, b): sh = len(a & b); return sh / (len(a) + len(b) - sh)
I = ["red cotton summer dress", "blue cotton summer shirt", "red wool winter scarf", "wool winter hat blue", "cotton summer dress floral"]; S = [wo(x) for x in I]
for i in range(len(I)):
    b = -1; bs = -1.0
    for j in range(len(I)):
        if i == j: continue
        s = ja(S[i], S[j])
        if s > bs: bs = s; b = j
    print(f"{I[i]} ~ {I[b]} ({bs:.3f})")
