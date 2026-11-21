def play(item, price):
    lo, hi = 1, 1000; steps = []; tries = 0
    while lo <= hi:
        g = (lo + hi) // 2; tries += 1
        if g < price: steps.append(f"{g} up"); lo = g + 1
        elif g > price: steps.append(f"{g} down"); hi = g - 1
        else: steps.append(f"{g} yes"); break
    print(f"{item}: {', '.join(steps)}")
    return tries
items = [("toaster", 39), ("bicycle", 640), ("headphones", 199), ("sofa", 999)]
t = sum(play(n, p) for n, p in items)
print(f"{t} guesses for {len(items)} items")
