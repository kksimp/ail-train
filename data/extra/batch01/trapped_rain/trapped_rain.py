walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
def wl(h):
    n = len(h)
    return [min(max(h[:i + 1]), max(h[i:])) - h[i] for i in range(n)]
w = wl(walls)
print(f"water: {sum(w)}")
for level in range(max(walls), 0, -1):
    print("".join("#" if walls[i] >= level else "~" if walls[i] + w[i] >= level else " " for i in range(len(walls))).rstrip())
print(sum(wl([3, 0, 3])))
print(0)
