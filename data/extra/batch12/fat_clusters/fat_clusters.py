FREE = 0
END = -1

def chain(fat, start):
    out = [start]
    c = start
    while fat[c] != END:
        c = fat[c]
        out.append(c)
    return out

def gaps(cs):
    return len([i for i in range(1, len(cs)) if cs[i] != cs[i - 1] + 1])

def write(fat, size):
    got = []
    for c in range(2, len(fat)):
        if fat[c] == FREE and len(got) < size:
            got.append(c)
    if len(got) < size:
        return -1
    for i in range(size - 1):
        fat[got[i]] = got[i + 1]
    fat[got[size - 1]] = END
    return got[0]

fat = [END, END, 3, 4, END, 6, 10, FREE, 11, FREE, 12, END, END, FREE, 15, 16, END, FREE]
files = {"report": 2, "photo": 5, "notes": 8, "song": 14}
for name, start in files.items():
    cs = chain(fat, start)
    print(f"{name:<7} clusters {cs}, {gaps(cs)} jumps")
for c in chain(fat, files["photo"]):
    fat[c] = FREE
del files["photo"]
print("deleted photo")
start = write(fat, 5)
files["video"] = start
vc = chain(fat, start)
print(f"video   clusters {vc}, {gaps(vc)} jumps")
free_left = len([c for c in range(2, len(fat)) if fat[c] == FREE])
print(f"{free_left} clusters free")
