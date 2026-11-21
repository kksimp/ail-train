def fold(dots, axis, line):
    out = set()
    for d in dots:
        x, y = d // 100, d % 100
        if axis == "x" and x > line: x = 2 * line - x
        if axis == "y" and y > line: y = 2 * line - y
        out.add(x * 100 + y)
    return out

text = "0,1 0,2 0,3 0,6 0,7 1,0 1,10 2,3 2,6 2,9 2,10 4,0 4,4 5,2 5,6 5,9 6,4 6,10 8,2 8,8 8,9 12,4 13,4 14,3 14,4 14,6 14,7 14,10 17,0 17,3 17,9 18,4 18,10 20,2 20,3 21,8 22,0"
dots = set()
for t in text.split(" "):
    x, y = t.split(","); dots.add(int(x) * 100 + int(y))
folds = ["y=5", "x=11"]
print(f"{len(dots)} dots before folding")
for i, f in enumerate(folds):
    a, b = f.split("=")
    dots = fold(dots, a, int(b))
    if i == 0:
        print(f"part 1: {len(dots)} dots after the first fold")
print(f"part 2: {len(dots)} dots read")
for y in range(5):
    print("".join('#' if x * 100 + y in dots else '.' for x in range(11)))
