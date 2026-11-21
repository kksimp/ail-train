def trim_bar(s):
    t = s
    if t.startswith("|"):
        t = t[1:]
    if t.endswith("|"):
        t = t[:-1]
    return t

def cells(line):
    inner = trim_bar(line.strip())
    return [c.strip() for c in inner.split("|")]

def align(text, w, how):
    gap = w - len(text)
    if how == "right":
        return " " * gap + text
    if how == "center":
        left = gap // 2
        return " " * left + text + " " * (gap - left)
    return text + " " * gap

def how_of(s):
    if s.startswith(":") and s.endswith(":"):
        return "center"
    if s.endswith(":"):
        return "right"
    return "left"

md = ["| Item | Qty | Price |", "|:-----|:---:|------:|", "| Apple | 3 | 1.20 |", "| Watermelon | 1 | 4.50 |", "| Fig | 12 | 0.35 |"]
header = cells(md[0])
hows = [how_of(s) for s in cells(md[1])]
body = [cells(l) for l in md[2:]]
widths = [len(h) for h in header]
for r in body:
    for j in range(len(r)):
        widths[j] = max(widths[j], len(r[j]))
rule = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
print(rule)
print("| " + " | ".join(align(header[j], widths[j], "center") for j in range(len(header))) + " |")
print(rule)
for r in body:
    print("| " + " | ".join(align(r[j], widths[j], hows[j]) for j in range(len(r))) + " |")
print(rule)
print(f"alignments: {', '.join(hows)}")
