lines = ["import os", "def load(path):", "    data = read(path)", "    if not data:", "        raise ValueError(path)", "    return data", "", "def save(path, data):", "    write(path, data)", "    log(path)", "", "def remove(name):", "    os.remove(name)"]
word = "path"
ctx = 1
show = set()
hits = set()
for i, l in enumerate(lines):
    if word in l:
        hits.add(i)
        for j in range(max(i - ctx, 0), min(i + ctx, len(lines) - 1) + 1):
            show.add(j)
last = -2
for i in sorted(show):
    if last >= 0 and i > last + 1:
        print("--")
    sep = ":" if i in hits else "-"
    print(f"{i + 1}{sep}{lines[i]}")
    last = i
print(f"{len(hits)} matching lines, {len(show)} shown")
