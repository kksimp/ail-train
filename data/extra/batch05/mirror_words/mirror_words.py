W = ["stressed", "level", "desserts", "drawer", "reward", "noon", "parts", "strap", "tops", "stop", "spot", "racecar", "live", "evil"]; P = set(W); pr = []; sf = []
for w in W:
    r = w[::-1]
    if r == w: sf.append(w)
    elif r in P and w < r: pr.append(f"{w}/{r}")
print(f"pairs: {', '.join(pr)}"); print(f"palindromes: {', '.join(sf)}")
