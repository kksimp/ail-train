def is_vowel(c):
    return c in "aeiouy"

def rhyme_key(word):
    cs = word.lower()
    n = len(cs)
    stop = n
    if n > 2 and cs[n - 1] == 'e' and not is_vowel(cs[n - 2]):
        stop = n - 1
    i = stop - 1
    while i > 0 and not is_vowel(cs[i]):
        i -= 1
    while i > 0 and is_vowel(cs[i - 1]):
        i -= 1
    return cs[i:]

def scheme(ends):
    keys = []
    out = []
    for w in ends:
        k = rhyme_key(w)
        if k not in keys:
            keys.append(k)
        out.append(chr(65 + keys.index(k)))
    return "".join(out)

forms = {"AABBA": "limerick", "ABAB": "alternate quatrain", "AABB": "couplets", "ABBA": "envelope quatrain", "ABABCDCDEFEFGG": "Shakespearean sonnet", "ABBAABBACDECDE": "Petrarchan sonnet"}
poems = [["tree", "bee", "day", "way", "see"], ["night", "tree", "bright", "free"], ["cat", "hat", "dog", "log"], ["moon", "sing", "ring", "soon"], ["day", "temperate", "May", "date", "shines", "dimmed", "declines", "untrimmed", "fade", "owest", "shade", "growest", "see", "thee"], ["hand", "free", "tree", "land", "stand", "see", "glee", "band", "bright", "shore", "rain", "night", "more", "plain"], ["rose", "blue", "sweet", "true"]]
for p in poems:
    s = scheme(p)
    name = forms.get(s, "no named form")
    print(f"{len(p):>2} lines {s:<15} {name}")
