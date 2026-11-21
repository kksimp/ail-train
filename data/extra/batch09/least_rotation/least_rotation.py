def least_start(cs):
    n = len(cs)
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        a = cs[(i + k) % n]
        b = cs[(j + k) % n]
        if a == b:
            k += 1
        else:
            if a > b:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                j += 1
            k = 0
    return min(i, j)

def canon(s):
    at = least_start(s)
    return s[at:] + s[:at]

codes = ["dcab", "bdca", "abdc", "cabd", "baba", "abab", "zyxzyw", "wzyxzy"]
groups = {}
for c in codes:
    print(f"{c:<7} starts at {least_start(c)} -> {canon(c)}")
    groups.setdefault(canon(c), []).append(c)
for key, members in groups.items():
    print(f"ring {key}: " + " ".join(members))
