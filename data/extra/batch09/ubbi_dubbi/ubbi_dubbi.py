def vowel(c):
    return c in "aeiou"

def encode_word(w):
    n = len(w)
    out = []
    prev = False
    for i, c in enumerate(w):
        v = vowel(c)
        silent = c == 'e' and i == n - 1 and n > 2 and not prev
        if v and not prev and not silent:
            out.append("ub")
        out.append(c)
        prev = v
    return "".join(out)

def decode_word(w):
    out = []
    i = 0
    while i < len(w):
        if i + 2 < len(w) and w[i] == 'u' and w[i + 1] == 'b' and vowel(w[i + 2]):
            i += 2
        else:
            out.append(w[i])
            i += 1
    return "".join(out)

for phrase in ["hello there", "ubbi dubbi", "make a cake", "queen of the sea", "round the moon"]:
    coded = " ".join(encode_word(w) for w in phrase.split(" "))
    back = " ".join(decode_word(w) for w in coded.split(" "))
    print(f"{phrase:<17} -> {coded:<28} -> {back}")
