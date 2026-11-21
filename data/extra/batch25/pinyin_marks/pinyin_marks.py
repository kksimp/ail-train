marks = {'a': "āáǎà", 'e': "ēéěè", 'i': "īíǐì", 'o': "ōóǒò", 'u': "ūúǔù", 'ü': "ǖǘǚǜ"}

def mark(syl):
    tone = int(syl[-1]) if syl[-1].isdigit() else 5
    letters = ['ü' if c == 'v' else c for c in syl[:-1]]
    if tone == 5:
        return "".join(letters)
    at = -1
    for i, c in enumerate(letters):
        if c == 'a' or c == 'e':
            at = i
        elif c == 'o' and i + 1 < len(letters) and letters[i + 1] == 'u' and at < 0:
            at = i
    if at < 0:
        for i, c in enumerate(letters):
            if c in marks:
                at = i
    out = list(letters)
    out[at] = marks[letters[at]][tone - 1]
    return "".join(out)

phrases = ["ni3 hao3", "zhong1 guo2", "xie4 xie5", "lv4 se4", "dui4 bu5 qi3", "shui3 jiao4", "liu2 xue2 sheng1", "gou3 you3"]
syllables = 0
for p in phrases:
    sylls = p.split(" ")
    syllables += len(sylls)
    marked = " ".join(mark(s) for s in sylls)
    print(f"{p:<16} {marked}")
print(f"{syllables} syllables marked")
