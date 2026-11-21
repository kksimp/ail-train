def dist(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        row = [i]
        for j in range(1, len(b) + 1):
            row.append(min(prev[j] + 1, row[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1])))
        prev = row
    return prev[-1]
d = ["receive", "separate", "definitely", "necessary", "weird", "calendar", "argument"]
for t in ["recieve", "seperate", "definately", "neccessary", "wierd", "calender", "arguement"]:
    b, bd = d[0], dist(t, d[0])
    for w in d[1:]:
        if dist(t, w) < bd: b, bd = w, dist(t, w)
    print(f"{t:<11} -> {b} ({bd})")
print(f"kitten/sitting: {dist('kitten', 'sitting')}")
