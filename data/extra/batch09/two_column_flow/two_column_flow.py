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
    if cur:
        lines.append(" ".join(cur))
    return lines

text = "Small town news: the bakery on Mill Lane reopens on Monday after a month of repairs, with the same bread, a new oven and longer hours on Saturday mornings for the market crowd."
width = 20
lines = pack(text, width)
half = (len(lines) + 1) // 2
for i in range(half):
    right = lines[i + half] if i + half < len(lines) else ""
    row = f"{lines[i]:<20}  |  {right}"
    print(row.rstrip())
print(f"{len(lines)} lines in two columns of {half}")
