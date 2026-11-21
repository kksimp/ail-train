def parse(line):
    p = line.split(" ")
    at = p[2].replace(":", "").split(",")
    size = p[3].split("x")
    return (int(p[0][1:]), int(at[0]), int(at[1]), int(size[0]), int(size[1]))

lines = ["#1 @ 1,1: 4x3", "#2 @ 3,2: 3x4", "#3 @ 8,0: 2x2", "#4 @ 0,5: 3x2", "#5 @ 5,4: 4x3", "#6 @ 2,6: 2x2"]
claims = [parse(l) for l in lines]
cover = {}
for cid, x0, y0, w, h in claims:
    for x in range(x0, x0 + w):
        for y in range(y0, y0 + h):
            cover[x * 100 + y] = cover.get(x * 100 + y, 0) + 1
print(f"{len(claims)} claims cover {len(cover)} square inches")
print(f"part 1: {sum(1 for n in cover.values() if n >= 2)} square inches are claimed twice or more")
for cid, x0, y0, w, h in claims:
    if all(cover[x * 100 + y] <= 1 for x in range(x0, x0 + w) for y in range(y0, y0 + h)):
        print(f"part 2: claim #{cid} overlaps nothing")
