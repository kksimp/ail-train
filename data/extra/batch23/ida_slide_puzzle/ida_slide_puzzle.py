def manhattan(b):
    h = 0
    for i in range(6):
        t = b[i]
        if t != 0:
            g = t - 1
            h += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return h

def search(b, blank, g, bound, prev, path, nodes):
    nodes[0] += 1
    f = g + manhattan(b)
    if f > bound:
        return f
    if f == g:
        return -1
    least = 1000
    r = blank // 3
    c = blank % 3
    for m in [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]:
        nr = r + m[0]
        nc = c + m[1]
        if 0 <= nr < 2 and 0 <= nc < 3:
            nb = nr * 3 + nc
            if nb != prev:
                b[blank], b[nb] = b[nb], b[blank]
                path.append(m[2])
                t = search(b, nb, g + 1, bound, blank, path, nodes)
                if t == -1:
                    return -1
                if t < least:
                    least = t
                path.pop()
                b[blank], b[nb] = b[nb], b[blank]
    return least

def ida(start):
    b = [int(ch) for ch in start]
    blank = b.index(0)
    bound = manhattan(b)
    path = []
    nodes = [0]
    rounds = 0
    while bound <= 30:
        rounds += 1
        t = search(b, blank, 0, bound, -1, path, nodes)
        if t == -1:
            moves = "".join(path)
            return f"{len(path)} moves {moves} ({rounds} rounds, {nodes[0]} nodes)"
        bound = t
    return "no solution within 30 moves"

print("goal 123450 (0 is the blank; moves name the way the blank goes)")
for s in ["123405", "412053", "241503", "023451", "012345", "530412"]:
    print(f"{s}: {ida(s)}")
