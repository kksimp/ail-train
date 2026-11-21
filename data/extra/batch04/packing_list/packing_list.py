I = [("tent", 2100, ["camp"], 10), ("stove", 800, ["camp"], 6), ("rain jacket", 400, ["camp", "city", "hike"], 9), ("camera", 700, ["city", "hike"], 5), ("boots", 1300, ["hike", "camp"], 8), ("book", 350, ["city", "camp"], 2), ("sun hat", 120, ["hike", "beach"], 4)]
for k, l in [("camp", 4500), ("hike", 2000), ("city", 3000)]:
    p = sorted([i for i in I if k in i[2]], key=lambda i: (-i[3], i[0]))
    while sum(i[1] for i in p) > l: p.pop()
    print(f"{k} ({l} g): {', '.join(i[0] for i in p)} = {sum(i[1] for i in p)} g")
