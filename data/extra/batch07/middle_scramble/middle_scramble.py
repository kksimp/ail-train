def sc(w):
    e = len(w)
    while e > 0 and not w[e - 1].isalpha(): e -= 1
    if e <= 3: return w
    return w[0] + w[1:e - 1][::-1] + w[e - 1:]
for l in ["according to research at a university, it does not matter", "the order of letters inside a word is less important", "only the first and last letters stay put!"]: print(" ".join(sc(w) for w in l.split(" ")))
