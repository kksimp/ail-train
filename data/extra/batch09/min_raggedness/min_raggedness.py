def line_len(ws, i, j):
    return j - i - 1 + sum(len(ws[k]) for k in range(i, j))

def greedy(ws, width):
    out = []
    start = 0
    for j in range(1, len(ws) + 1):
        if line_len(ws, start, j) > width:
            out.append([start, j - 1])
            start = j - 1
    out.append([start, len(ws)])
    return out

def best(ws, width):
    n = len(ws)
    cost = [0] * (n + 1)
    choice = [n] * (n + 1)
    i = n - 1
    while i >= 0:
        cost[i] = -1
        for j in range(i + 1, n + 1):
            used = line_len(ws, i, j)
            if used > width:
                break
            spare = width - used
            here = 0 if j == n else spare * spare
            if cost[i] < 0 or here + cost[j] < cost[i]:
                cost[i] = here + cost[j]
                choice[i] = j
        i -= 1
    out = []
    at = 0
    while at < n:
        out.append([at, choice[at]])
        at = choice[at]
    return out

def show(ws, lines, width, name):
    total = 0
    for k, l in enumerate(lines):
        text = " ".join(ws[l[0]:l[1]])
        if k < len(lines) - 1:
            spare = width - len(text)
            total += spare * spare
        print(text.ljust(width) + "|")
    print(f"{name}: badness {total}")

ws = "a bird in the hand is worth two in the bush they say".split(" ")
show(ws, greedy(ws, 12), 12, "greedy")
show(ws, best(ws, 12), 12, "balanced")
