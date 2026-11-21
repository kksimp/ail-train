space = [[0, 4, 2, 6], [3, 1, 8, 0], [5, 9, 2, 7]]
def place(need):
    for a in range(len(space)):
        for l in range(len(space[a])):
            if space[a][l] >= need:
                space[a][l] -= need
                return f"aisle {a + 1} level {l + 1}"
    return "nowhere"
for name, need in [("TV", 7), ("lamp", 2), ("rug", 9), ("piano", 12), ("vase", 6)]:
    print(f"{name} ({need}): {place(need)}")
for i, a in enumerate(space):
    print(f"aisle {i + 1} free: {a}")
print(f"free volume left: {sum(sum(a) for a in space)}")
