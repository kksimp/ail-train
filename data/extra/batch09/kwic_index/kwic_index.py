titles = ["The Old Man and the Sea", "A Tale of Two Cities", "The Man in the Iron Mask", "Sea of Tranquility"]
stop = {"the", "a", "and", "of", "in"}
entries = []
for t in titles:
    ws = t.split(" ")
    for i, w in enumerate(ws):
        if w.lower() not in stop:
            entries.append((w, " ".join(ws[:i]), " ".join(ws[i + 1:])))
for key, left, right in sorted(entries, key=lambda e: (e[0].lower(), e[1])):
    if len(left) > 16:
        left = left[len(left) - 16:]
    line = f"{left:>16} [{key}] {right}"
    print(line.rstrip())
