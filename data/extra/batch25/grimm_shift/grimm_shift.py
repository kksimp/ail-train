def segments(w):
    out = []
    i = 0
    while i < len(w):
        c = w[i]
        if i + 1 < len(w) and w[i + 1] == 'h' and c in "bdg":
            out.append(c + "h")
            i += 2
        else:
            out.append(c)
            i += 1
    return out

def pick(s, frm, to):
    if s in frm:
        return to[frm.index(s)]
    return s

def shift(w, natural):
    rules = [[["p", "t", "k"], ["f", "þ", "h"]], [["b", "d", "g"], ["p", "t", "k"]], [["bh", "dh", "gh"], ["b", "d", "g"]]]
    segs = segments(w)
    for step in range(3):
        r = rules[step] if natural else rules[2 - step]
        segs = [pick(s, r[0], r[1]) for s in segs]
    return "".join(segs)

words = ["pater", "treyes", "kerd", "dekm", "bhrater", "genu", "yugom", "dhur", "pod", "ghans"]
differ = 0
for w in words:
    good = shift(w, True)
    bad = shift(w, False)
    note = "" if good == bad else f", feeding order gives {bad}"
    if good != bad:
        differ += 1
    print(f"{w:<8} -> {good}{note}")
print(f"{differ} of {len(words)} words depend on the rule order")
