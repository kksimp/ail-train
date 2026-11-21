rules = [("steam", "air", "cloud"), ("lava", "water", "stone"), ("fire", "earth", "lava"), ("fire", "water", "steam"), ("earth", "water", "mud"), ("mud", "fire", "brick"), ("stone", "stone", "wall")]
bag = {"fire": 4, "water": 5, "earth": 3, "air": 1}
def fires(bag, r):
    a, b, _ = r
    if a == b: return bag.get(a, 0) >= 2
    return bag.get(a, 0) >= 1 and bag.get(b, 0) >= 1
step = 0
while True:
    r = next((r for r in rules if fires(bag, r)), None)
    if r is None: break
    a, b, m = r
    bag[a] = bag.get(a, 0) - 1
    bag[b] = bag.get(b, 0) - 1
    bag[m] = bag.get(m, 0) + 1
    step += 1
    print(f"{step:>2}. {a} + {b} -> {m}")
left = [f"{k} {bag[k]}" for k in bag if bag[k] > 0]
print(f"left in the bag: {', '.join(left)}")
