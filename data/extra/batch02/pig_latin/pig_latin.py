def pig(w):
    if not w: return w
    if w[0].lower() in "aeiou": return w + "way"
    k = 0
    while k < len(w) and w[k].lower() not in "aeiou": k += 1
    if 0 < k < len(w) and w[k - 1].lower() == "q" and w[k].lower() == "u": k += 1
    m = w[k:] + w[:k].lower() + "ay"
    if w[0].isupper(): m = m[0].upper() + m[1:]
    return m
for s in ["Hello world", "apple pie", "Queen square", "rhythm and blues", "String theory"]:
    print(f"{s} -> {' '.join(pig(x) for x in s.split())}")
