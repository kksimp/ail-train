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

def find_all(text, pat):
    joined = f"{pat}|{text}"
    z = z_array(joined)
    m = len(pat)
    return [i - m - 1 for i in range(m + 1, len(z)) if z[i] >= m]

sample = "aabcaabxaaaz"
z = z_array(sample)
print(f"{sample}: " + " ".join(str(v) for v in z))
text = "GATTACAGATTAGATTACA"
for pat in ["GATTA", "TTA", "ACA", "CAT"]:
    hits = find_all(text, pat)
    spots = "none" if not hits else ", ".join(str(h) for h in hits)
    print(f"{pat:<6} at {spots}")
