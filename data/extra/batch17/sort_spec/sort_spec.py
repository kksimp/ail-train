class Entry:
    def __init__(self, name, ext, size):
        self.name, self.ext, self.size = name, ext, size

def cmp3(x, y):
    return -1 if x < y else 1 if x > y else 0

def compare_key(a, b, key):
    if key == "size":
        return cmp3(a.size, b.size)
    if key == "ext":
        return cmp3(a.ext, b.ext)
    return cmp3(a.name, b.name)

def compare(a, b, spec):
    for part in spec.split(","):
        desc = part.startswith("-")
        key = part[1:] if desc else part
        c = compare_key(a, b, key)
        if c != 0:
            return -c if desc else c
    return 0

def sort_by_spec(xs, spec):
    for i in range(1, len(xs)):
        j = i
        while j > 0 and compare(xs[j - 1], xs[j], spec) > 0:
            xs[j - 1], xs[j] = xs[j], xs[j - 1]
            j -= 1

files = [Entry("notes", "txt", 12), Entry("photo", "jpg", 2048), Entry("app", "js", 300), Entry("data", "csv", 2048), Entry("readme", "txt", 4), Entry("logo", "png", 300)]
for spec in ["-size,name", "-ext,size", "name"]:
    xs = list(files)
    sort_by_spec(xs, spec)
    shown = " ".join(f"{e.name}.{e.ext}({e.size})" for e in xs)
    print(f"{spec:<11} {shown}")
