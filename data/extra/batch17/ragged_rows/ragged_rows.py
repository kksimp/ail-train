def repair(fields, width):
    if len(fields) == width:
        return fields
    if len(fields) < width:
        out = list(fields)
        while len(out) < width:
            out.append("")
        return out
    out2 = fields[:width - 1]
    out2.append(",".join(fields[width - 1:]))
    return out2

header = "date,user,action,comment".split(",")
lines = ["2025-03-01,ana,login,", "2025-03-01,ben,upload", "2025-03-02,ana,comment,nice, very nice", "2025-03-02,cy", "2025-03-03,ben,logout,bye"]
w = len(header)
fixed = []
for i, line in enumerate(lines):
    fields = line.split(",")
    if len(fields) < w:
        print(f"row {i + 1}: {w - len(fields)} missing, padded")
    elif len(fields) > w:
        print(f"row {i + 1}: {len(fields) - w} extra, joined into {header[w - 1]}")
    fixed.append(repair(fields, w))
widths = [len(h) for h in header]
for r in fixed:
    for j in range(w):
        widths[j] = max(widths[j], len(r[j]))
for r in [header] + fixed:
    cells = [r[j].ljust(widths[j], ' ') for j in range(w)]
    print(" | ".join(cells).rstrip())
