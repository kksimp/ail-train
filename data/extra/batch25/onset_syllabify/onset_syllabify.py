def is_vowel(c):
    return c in "aeiouy"

def legal(s, onsets):
    return (len(s) == 1 and s != "x") or s in onsets

def syllabify(w, onsets):
    n = len(w)
    sylls = []
    cur = []
    i = 0
    while i < n and not is_vowel(w[i]):
        cur.append(w[i])
        i += 1
    while i < n:
        while i < n and is_vowel(w[i]):
            cur.append(w[i])
            i += 1
        cluster = []
        while i < n and not is_vowel(w[i]):
            cluster.append(w[i])
            i += 1
        if i == n:
            cur.extend(cluster)
            break
        k = 0
        while k < len(cluster) and not legal("".join(cluster[k:]), onsets):
            k += 1
        cur.extend(cluster[:k])
        sylls.append("".join(cur))
        cur = cluster[k:]
    sylls.append("".join(cur))
    return ".".join(sylls)

onsets = {"pl", "pr", "tr", "dr", "kl", "kr", "cl", "cr", "bl", "br", "gl", "gr", "fl", "fr", "st", "str", "sp", "spr", "sk", "sl", "sm", "sn", "sw", "tw"}
words = ["extra", "instrument", "pumpkin", "lobster", "acrobat", "pilgrim", "atlas", "empty", "sandwich", "explain"]
total = 0
for w in words:
    s = syllabify(w, onsets)
    count = len(s.split("."))
    total += count
    print(f"{w:<11} {s} ({count})")
print(f"{total} syllables in {len(words)} words")
