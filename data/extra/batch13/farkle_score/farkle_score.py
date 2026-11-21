def score(dice):
    c = [0] * 7
    for d in dice:
        c[d] += 1
    if len(dice) == 6 and all(n == 1 for n in c[1:]):
        return [1500, 6]
    if len(dice) == 6 and sum(1 for n in c if n == 2) == 3:
        return [750, 6]
    points = 0
    used = 0
    for face in range(1, 7):
        n = c[face]
        if n >= 3:
            part = 1000 if face == 1 else face * 100
            for k in range(3, n):
                part *= 2
            points += part
            used += n
            n = 0
        if face == 1:
            points += n * 100
            used += n
        if face == 5:
            points += n * 50
            used += n
    return [points, used]

throws = [[1, 5, 2, 3, 4, 6], [2, 2, 3, 3, 6, 6], [1, 1, 1, 5, 2, 4], [4, 4, 4, 4, 2, 3], [2, 3, 4, 6, 6, 3], [5, 5, 5, 5, 5, 1], [3, 4, 6, 2], [1, 5, 5]]
farkles = 0
for t in throws:
    s = score(t)
    shown = " ".join(str(x) for x in t)
    if s[0] == 0:
        farkles += 1
        print(f"{shown:<11} farkle")
    else:
        print(f"{shown:<11} {s[0]:>5} using {s[1]} dice")
print(f"farkles: {farkles} of {len(throws)}")
