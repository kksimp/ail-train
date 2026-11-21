def middle(xs):
    if not xs:
        return None
    s = sorted(xs)
    return s[(len(s) - 1) // 2]
prices = [325000, 289000, 410000, 298500, 352000]
print(f"middle asking price: {middle(prices):,}")
print(f"middle viewing slot: {middle(['14:30', '09:15', '11:00', '16:45'])}")
offers = [(310000, "Lee"), (305000, "Diaz"), (318000, "Kaur")]
o = middle(offers)
print(f"middle offer: {o[0]:,} from {o[1]}")
top = max(offers)
print(f"best offer: {top[0]:,} from {top[1]}")
print("no sales yet: -1")
