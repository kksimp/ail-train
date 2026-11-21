text = """41   37
18   41
25   25
41   12
9    41
30   18"""
left = []; right = []
for line in text.splitlines():
    w = line.split()
    left.append(int(w[0])); right.append(int(w[1]))
ls = sorted(left); rs = sorted(right)
gap = 0
for i in range(len(ls)):
    d = abs(ls[i] - rs[i])
    print(f"{ls[i]:>3} {rs[i]:>3}  gap {d}")
    gap += d
print(f"part 1: total gap {gap}")
counts = {}
for r in right:
    counts[r] = counts.get(r, 0) + 1
print(f"part 2: similarity score {sum(x * counts.get(x, 0) for x in left)}")
