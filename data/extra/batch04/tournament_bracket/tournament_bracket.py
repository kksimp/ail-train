R = {"Aki": 2710, "Bram": 2650, "Cleo": 2690, "Dana": 2600, "Esa": 2580, "Finn": 2640, "Gia": 2700, "Hugo": 2550}
s = sorted(R, key=lambda p: (-R[p], p)); f = [s[i] for i in [0, 7, 3, 4, 1, 6, 2, 5]]; rd = 1
while len(f) > 1:
    f = [f[i] if R[f[i]] >= R[f[i + 1]] else f[i + 1] for i in range(0, len(f), 2)]
    print(f"round {rd}: {', '.join(f)}"); rd += 1
print(f"champion: {f[0]}")
