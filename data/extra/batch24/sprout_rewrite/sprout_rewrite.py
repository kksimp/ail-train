def rewrite(s):
    return "".join("S[SL]" if ch == 'S' else "LF" if ch == 'L' else ch for ch in s)
def depth(s):
    d = 0; most = 0
    for ch in s:
        if ch == '[': d += 1; most = max(most, d)
        elif ch == ']': d -= 1
    return most
plant = "S"
for gen in range(6):
    print(f"gen {gen}: length {len(plant):>3}, stems {plant.count('S'):>2}, leaves {plant.count('L'):>2}, flowers {plant.count('F'):>2}, depth {depth(plant)}")
    if gen == 2: print(f"  {plant}")
    plant = rewrite(plant)
