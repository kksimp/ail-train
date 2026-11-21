def interleave(a, b, c):
    la, lb = len(a), len(b)
    if la + lb != len(c):
        return "no (lengths differ)"
    ok = [[False] * (lb + 1) for _ in range(la + 1)]
    ok[0][0] = True
    for i in range(la + 1):
        for j in range(lb + 1):
            if i > 0 and ok[i - 1][j] and a[i - 1] == c[i + j - 1]:
                ok[i][j] = True
            if j > 0 and ok[i][j - 1] and b[j - 1] == c[i + j - 1]:
                ok[i][j] = True
    if not ok[la][lb]:
        return "no"
    marks = []
    i, j = la, lb
    while i + j > 0:
        if i > 0 and ok[i - 1][j] and a[i - 1] == c[i + j - 1]:
            marks.append("1")
            i -= 1
        else:
            marks.append("2")
            j -= 1
    marks.reverse()
    return "yes " + "".join(marks)

cases = [("abc", "def", "adbecf"), ("aabcc", "dbbca", "aadbbcbcac"), ("aabcc", "dbbca", "aadbbbaccc"), ("cat", "dog", "cdaotg"), ("hi", "yo", "hiyox")]
for a, b, c in cases:
    print(f"{a} + {b} -> {c}: {interleave(a, b, c)}")
