def pack(text, width):
    lines = []
    cur = []
    used = 0
    for w in text.split(" "):
        extra = len(w) if not cur else len(w) + 1
        if used + extra > width and cur:
            lines.append(" ".join(cur))
            cur = [w]
            used = len(w)
        else:
            cur.append(w)
            used += extra
    lines.append(" ".join(cur))
    return lines

def flip(s):
    return s[::-1]

text = "the plough turns at the end of each furrow and comes back the other way so the reader never jumps back"
width = 22
lines = pack(text, width)
carved = []
for i, l in enumerate(lines):
    row = l if i % 2 == 0 else flip(l).rjust(width)
    carved.append(row)
    print(row)
read = []
for i, row in enumerate(carved):
    read.append(row if i % 2 == 0 else flip(row.lstrip()))
same = " ".join(read) == text
print(f"read back matches: {'true' if same else 'false'}")
