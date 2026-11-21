folded = ["main;load;read 40", "main;load;parse 25", "main;run;step;alloc 10", "main;run;step 50", "main;run;gc 15", "main;load;read 5", "main;save 5"]
total = {}
self_count = {}
order = []
all_ = 0
for line in folded:
    sp = line.rfind(" ")
    stack = line[:sp].split(";")
    n = int(line[sp + 1:])
    all_ += n
    for i in range(len(stack)):
        path = ";".join(stack[:i + 1])
        if path not in total:
            order.append(path)
        total[path] = total.get(path, 0) + n
    k = ";".join(stack)
    self_count[k] = self_count.get(k, 0) + n
ordered = sorted(order)
for p in ordered:
    parts = p.split(";")
    depth = len(parts) - 1
    name = parts[depth]
    pct = float(total[p] * 1000 // all_) / 10.0
    label = "  " * depth + name
    print(f"{label:<16} {total[p]:>4} {pct:>5.1f}%  self {self_count.get(p, 0)}")
hottest = sorted(self_count.keys(), key=lambda k: -self_count[k])[0]
print(f"hottest frame: {hottest} ({self_count[hottest]} samples)")
