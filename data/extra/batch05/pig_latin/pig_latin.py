def w(x):
    if not x: return x
    if x[0] in "aeiou": return x + "way"
    i = 0
    while i < len(x) and x[i] not in "aeiou":
        if x[i] == "q" and i + 1 < len(x) and x[i + 1] == "u": i += 2; break
        i += 1
    return x[i:] + x[:i] + "ay"
for l in ["the quick brown fox", "i eat apples, then sleep.", "strength through rhythm"]:
    o = []
    for r in l.split(" "):
        t = ""; c = r
        if r.endswith(",") or r.endswith("."): t = r[-1]; c = r[:-1]
        o.append(w(c) + t)
    print(" ".join(o))
