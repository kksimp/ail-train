def z_array(cs):
    n = len(cs)
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and cs[z[i]] == cs[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

def find_all(pattern, text):
    joined = f"{pattern}|{text}"
    z = z_array(list(joined))
    m = len(pattern)
    start = m + 1
    hits = []
    for i in range(start, len(z)):
        if z[i] == m:
            hits.append(i - start)
    return hits

text = "abracadabra cadabra abra"
print(f"text: {text}")
for p in ["abra", "cad", "bra c", "dab", "a", "zz"]:
    hits = find_all(p, text)
    print(f"{p:<6} found {len(hits)} times at {hits}")
z = z_array(list("aabxaab"))
print(f"z of aabxaab: {z}")
