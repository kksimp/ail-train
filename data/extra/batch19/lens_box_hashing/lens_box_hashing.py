def hsh(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h

steps = "pq=4,rm-,zx=2,pq-,tk=7,zx=5,ab=1,cd=3,ab-,ef=6,pq=8".split(",")
print(f"part 1: hash sum {sum(hsh(s) for s in steps)}")
boxes = {}
for st in steps:
    if st.endswith("-"):
        label = st[:-1]; b = hsh(label)
        if b in boxes:
            boxes[b] = [l for l in boxes[b] if l[0] != label]
    else:
        label, f = st.split("="); f = int(f); b = hsh(label)
        lenses = boxes.get(b, [])
        placed = False
        for l in lenses:
            if l[0] == label:
                l[1] = f; placed = True
        if not placed:
            lenses.append([label, f])
        boxes[b] = lenses
power = 0
for b in sorted(boxes):
    for i, l in enumerate(boxes[b]):
        print(f"box {b} slot {i + 1}: {l[0]} {l[1]}")
        power += (b + 1) * (i + 1) * l[1]
print(f"part 2: focusing power {power}")
