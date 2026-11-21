def nt(s):
    o = ""; i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        o += f"{j - i}{s[i]}"; i = j
    return o
s = "1"; L = []
for n in range(1, 21):
    if n <= 8: print(f"{n}: {s}")
    L.append(len(s)); s = nt(s)
for n in [10, 15, 20]: print(f"len {n}: {L[n - 1]} (ratio {L[n - 1] / L[n - 2]:.3f})")
