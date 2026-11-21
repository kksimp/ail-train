S = [(3, 3, 3), (10, 5, 4), (17, 2, 2), (16, 8, 2)]; dr = db = 0
for y in range(10):
    ln = ""
    for x in range(20):
        h = sum(1 for s in S if (x - s[0]) ** 2 + (y - s[1]) ** 2 <= s[2] ** 2)
        if h == 0: dr += 1; ln += "."
        else:
            if h > 1: db += 1
            ln += str(h)
    print(ln)
print(f"{dr} dry cells, {db} watered twice or more, {200 - dr} of 200 covered")
