def sold(m, p):
    return max(m[0] - m[1] * p, 0)

def profit(ms, p):
    return sum((p - 10) * sold(m, p) for m in ms)

def best_price(ms):
    best = 10
    for p in range(10, 61):
        if profit(ms, p) > profit(ms, best):
            best = p
    return best

home = (100, 2)
away = (60, 1)
p1 = best_price([home])
p2 = best_price([away])
split = profit([home], p1) + profit([away], p2)
print(f"home market: price {p1}, sells {sold(home, p1)}, profit {profit([home], p1)}")
print(f"away market: price {p2}, sells {sold(away, p2)}, profit {profit([away], p2)}")
both = [home, away]
p = best_price(both)
one = profit(both, p)
print(f"one price for both: {p}, sells {sold(home, p)} + {sold(away, p)}, profit {one}")
print(f"separate prices earn {split - one} more")
