import math
state = 9001
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def d2(a, b): return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
stars = []; refused = 0
for k in range(70):
    p = [below(40), below(20)]
    if any(d2(s, p) < 20 for s in stars): refused += 1
    else: stars.append(p)
for row in range(10):
    print("".join('*' if any(s[0] == col and s[1] // 2 == row for s in stars) else '.' for col in range(40)))
best = 100000
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        best = min(best, d2(stars[i], stars[j]))
gap = math.sqrt(best)
print(f"{len(stars)} stars kept, {refused} refused, closest pair {gap:.3f} apart")
