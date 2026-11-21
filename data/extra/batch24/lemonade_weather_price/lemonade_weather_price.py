def cups(weather, price):
    n = 120 - price if weather == 0 else 80 - price if weather == 1 else 40 - price // 2
    return max(n, 0)
def profit(weather, price): return cups(weather, price) * (price - 20)
def best_price(weather):
    pick = 20
    for p in range(20, 121):
        if profit(weather, p) > profit(weather, pick): pick = p
    return pick
names = ["sunny", "cloudy", "rainy"]
tuned = []
for w in range(3):
    p = best_price(w); tuned.append(p)
    print(f"{names[w]:<6}: best price {p} cents, {cups(w, p)} cups, profit {profit(w, p)}")
days = [0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0]
flexible = sum(profit(w, tuned[w]) for w in days)
fixed = sum(profit(w, tuned[0]) for w in days)
print(f"two weeks: weather prices earn {flexible}, the sunny price every day earns {fixed}")
