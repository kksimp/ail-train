def be(h):
    s = []; t = (0, 0, 0)
    for i in range(len(h) + 1):
        c = 0 if i == len(h) else h[i]
        while s and h[s[-1]] >= c:
            j = s.pop(); l = 0 if not s else s[-1] + 1; a = h[j] * (i - l)
            if a > t[0]: t = (a, l, i - 1)
        s.append(i)
    return t
for B in [[2, 1, 5, 6, 2, 3], [6, 2, 5, 4, 5, 1, 6], [3, 3, 3, 3], [1, 2, 3, 4, 5], [7]]:
    b = be(B); print(f"[{' '.join(map(str, B))}]: area {b[0]}, bars {b[1]}..{b[2]}")
