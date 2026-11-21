def marked(price, age):
    pct = {0: 100, 1: 70, 2: 40}.get(age, 0)
    return price * pct // 100 // 5 * 5

def money(c):
    return f"{c // 100}.{c % 100:02d}"

today = 10
shelf = [("sourdough", 10, 420, 6), ("baguette", 9, 180, 8), ("croissant", 9, 145, 12), ("rye loaf", 8, 395, 3), ("scone", 7, 120, 10), ("bloomer", 10, 250, 5), ("focaccia", 8, 299, 4)]
value = donated = 0
for name, baked, price, left in shelf:
    age = today - baked
    now = marked(price, age)
    if now == 0:
        donated += left
        print(f"{name:<9} baked {age} days ago: {left} to the food bank")
    else:
        value += now * left
        print(f"{name:<9} {left:>2} at {money(now)} (was {money(price)})")
print(f"shelf worth {money(value)}; {donated} items donated")
