weights = [64, 58, 71, 49, 66, 75, 61, 68, 70, 55, 63, 77, 52, 69, 60, 65, 72, 59, 66, 74, 67, 62, 53, 70]
def grade(g):
    return "S" if g < 53 else "M" if g < 63 else "L" if g < 73 else "XL"
groups = {}
for w in weights: groups.setdefault(grade(w), []).append(w)
c = 0
for g in ["S", "M", "L", "XL"]:
    eggs = groups.get(g, [])
    boxes = [eggs[i:i + 6] for i in range(0, len(eggs), 6)]
    c += len(boxes)
    part = [b for b in boxes if len(b) < 6]
    note = "all full" if not part else f"one holds {len(part[0])}"
    print(f"{g:<2} {len(eggs):>2} eggs -> {len(boxes)} cartons, {note}")
print(f"{len(weights)} eggs in {c} cartons, heaviest {max(weights)} g")
