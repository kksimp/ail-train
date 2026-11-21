def copies(have, need):
    most = 1000000
    for part, n in need.items():
        most = min(most, have.get(part, 0) // n)
    return most

have = {"2x4 red": 14, "2x2 red": 6, "1x2 grey": 22, "wheel": 4, "axle": 1, "window": 3, "2x4 blue": 9, "plate 6x8": 2}
sets = [("fire truck", {"2x4 red": 8, "2x2 red": 4, "wheel": 4, "axle": 2, "window": 1}), ("cottage", {"2x4 blue": 6, "1x2 grey": 10, "window": 3, "plate 6x8": 1}), ("tower", {"1x2 grey": 12, "2x2 red": 2, "plate 6x8": 1}), ("bridge", {"plate 6x8": 3, "2x4 red": 4})]
for name, need in sets:
    n = copies(have, need)
    if n > 0:
        print(f"{name}: can build {n}")
    else:
        short = []
        for part, k in need.items():
            gap = k - have.get(part, 0)
            if gap > 0:
                short.append(f"{gap} x {part}")
        missing = ", ".join(short)
        print(f"{name}: missing {missing}")
