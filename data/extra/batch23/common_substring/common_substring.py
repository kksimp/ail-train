def common(a, b):
    xs = list(a)
    ys = list(b)
    width = len(ys) + 1
    prev = [0] * width
    best = 0
    end_a = 0
    for i in range(1, len(xs) + 1):
        cur = [0]
        for j in range(1, len(ys) + 1):
            v = prev[j - 1] + 1 if xs[i - 1] == ys[j - 1] else 0
            cur.append(v)
            if v > best:
                best = v
                end_a = i
        prev = cur
    return a[end_a - best:end_a]

pairs = [("GATTACAGT", "CTTACAGA"), ("photograph", "telegraph"), ("interstellar", "stellarator"), ("abc", "xyz"), ("sunflower", "mayflower"), ("rhythm", "algorithm")]
for a, b in pairs:
    c = common(a, b)
    print(f"{a:<13} {b:<12} -> [{c}] length {len(c)}")
