text = "The cat sat. It was warm in the sun! Why would anyone move from such a lovely spot? Nobody knows"
ss, cur = [], ""
for c in text:
    cur += c
    if c in ".!?":
        if cur.strip(): ss.append(cur.strip())
        cur = ""
if cur.strip(): ss.append(cur.strip())
cw = lambda s: [x for x in ("".join(c for c in w if c.isalpha()) for w in s.split()) if x]
aw = []
for s in ss:
    ws = cw(s); print(f"{len(ws):>2} words: {s}"); aw += ws
avg = sum(map(len, aw)) / len(aw)
print(f"{len(ss)} sentences, {len(aw)} words, {len(aw) // len(ss)} per sentence, {avg:.1f} letters per word")
print("longest: " + max(ss, key=lambda s: len(cw(s))))
