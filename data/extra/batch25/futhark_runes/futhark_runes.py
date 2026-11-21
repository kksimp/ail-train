def to_runes(word, m):
    cs = word.lower()
    out = []
    i = 0
    while i < len(cs):
        if i + 1 < len(cs):
            pair = cs[i] + cs[i + 1]
            if pair in m:
                out.append(m[pair])
                i += 2
                continue
        one = cs[i]
        out.append(m.get(one, one))
        i += 1
    return "".join(out)

def from_runes(text, back):
    return "".join(back.get(c, "?") for c in text)

pairs = [("f", "ᚠ"), ("u", "ᚢ"), ("th", "ᚦ"), ("a", "ᚨ"), ("r", "ᚱ"), ("k", "ᚲ"), ("g", "ᚷ"), ("w", "ᚹ"), ("h", "ᚺ"), ("n", "ᚾ"), ("i", "ᛁ"), ("j", "ᛃ"), ("ei", "ᛇ"), ("p", "ᛈ"), ("z", "ᛉ"), ("s", "ᛊ"), ("t", "ᛏ"), ("b", "ᛒ"), ("e", "ᛖ"), ("m", "ᛗ"), ("l", "ᛚ"), ("ng", "ᛜ"), ("o", "ᛟ"), ("d", "ᛞ"), ("c", "ᚲ"), ("q", "ᚲ"), ("v", "ᚹ"), ("y", "ᛃ"), ("x", "ᚲᛊ")]
m = {}
back = {}
for latin, rune in pairs:
    m[latin] = rune
    if rune not in back:
        back[rune] = latin
for w in ["Thor", "Freya", "King", "Odin", "Heimdall", "Quick", "Viking", "Alex"]:
    r = to_runes(w, m)
    print(f"{w:<9} {r:<9} back: {from_runes(r, back)}")
print(f"{len(back)} distinct runes used")
