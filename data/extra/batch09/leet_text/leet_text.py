def to_leet(text):
    table = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return "".join(table.get(c, c) for c in text.lower())

def readings(word):
    back = {'4': 'a', '3': 'e', '0': 'o', '5': 's', '7': 't'}
    out = [""]
    for c in word:
        nxt = []
        for prefix in out:
            if c == '1':
                nxt.append(prefix + "i")
                nxt.append(prefix + "l")
            else:
                nxt.append(prefix + back.get(c, c))
        out = nxt
    return out

known = {"little", "toast", "elite", "listen", "silent", "steel", "tile", "lost", "is", "steal", "list"}
for phrase in ["elite toast", "listen", "silent steel"]:
    print(f"{phrase:<13} -> {to_leet(phrase)}")
for code in ["1i771e", "5113n7", "1i57", "71135"]:
    options = readings(code)
    hits = [w for w in options if w in known]
    shown = "unknown" if not hits else " or ".join(hits)
    print(f"{code:<7} {len(options)} readings -> {shown}")
