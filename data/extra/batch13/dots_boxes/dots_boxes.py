def sides(r, c):
    return [f"h{r}{c}", f"h{r + 1}{c}", f"v{r}{c}", f"v{r}{c + 1}"]

def complete(lines, r, c):
    return all(x in lines for x in sides(r, c))

all_lines = []
for r in range(4):
    for c in range(3):
        all_lines.append(f"h{r}{c}")
for r in range(3):
    for c in range(4):
        all_lines.append(f"v{r}{c}")
seed = 31
i = len(all_lines) - 1
while i > 0:
    seed = (seed * 1103515245 + 12345) % 2147483648
    j = seed % (i + 1)
    all_lines[i], all_lines[j] = all_lines[j], all_lines[i]
    i -= 1
names = ["Ada", "Bo"]
drawn = set()
score = [0, 0]
p = 0
for line in all_lines:
    drawn.add(line)
    closed = 0
    for r in range(3):
        for c in range(3):
            if line in sides(r, c) and complete(drawn, r, c):
                closed += 1
                print(f"{names[p]} draws {line} and closes box {r},{c}")
    score[p] += closed
    if closed == 0:
        p = 1 - p
print(f"{names[0]} {score[0]}, {names[1]} {score[1]}")
