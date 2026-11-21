def vowel(c):
    return c in "aeiouy"

def syllables(word):
    count = 0
    prev = False
    for c in word:
        v = vowel(c)
        if v and not prev:
            count += 1
        prev = v
    if word.endswith("e") and count > 1:
        count -= 1
    return count

def forms(adj):
    irregular = {"good": ["better", "best"], "bad": ["worse", "worst"], "far": ["farther", "farthest"]}
    if adj in irregular:
        return irregular[adj]
    s = syllables(adj)
    n = len(adj)
    if s >= 3 or (s == 2 and not adj.endswith("y")):
        return [f"more {adj}", f"most {adj}"]
    stem = adj
    if adj.endswith("e"):
        stem = adj[:n - 1]
    elif adj.endswith("y") and s == 2:
        stem = adj[:n - 1] + "i"
    elif n >= 3 and not vowel(adj[n - 1]) and vowel(adj[n - 2]) and not vowel(adj[n - 3]) and adj[n - 1] not in "wx":
        stem = adj + adj[n - 1]
    return [stem + "er", stem + "est"]

for adj in ["tall", "large", "big", "happy", "busy", "careful", "beautiful", "good", "bad", "far", "thin", "slow", "modern"]:
    f = forms(adj)
    print(f"{adj:<10} {syllables(adj)} syllable(s): {f[0]:<15} {f[1]}")
