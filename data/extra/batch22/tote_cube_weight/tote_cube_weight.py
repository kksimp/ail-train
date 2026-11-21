items = [("books", 12, 95), ("towels", 18, 20), ("pans", 15, 60), ("jars", 8, 70), ("pillow", 30, 10), ("lamp", 14, 25), ("tins", 6, 55), ("rug", 25, 40), ("mugs", 9, 30), ("shoes", 16, 15)]

def pack(items):
    totes = []
    for name, l, w in items:
        placed = False
        for t in totes:
            if not placed and t[1] + l <= 50 and t[2] + w <= 150:
                t[0].append(name)
                t[1] += l
                t[2] += w
                placed = True
        if not placed:
            totes.append([[name], l, w])
    return totes

def show(totes):
    for names, l, w in totes:
        quoted = ", ".join(names)
        print(f"  {quoted}: {l} l, {w // 10}.{w % 10} kg")

bv = pack(sorted(items, key=lambda i: -i[1]))
bw = pack(sorted(items, key=lambda i: -i[2]))
print(f"sorted by volume: {len(bv)} totes")
show(bv)
print(f"sorted by weight: {len(bw)} totes")
show(bw)
