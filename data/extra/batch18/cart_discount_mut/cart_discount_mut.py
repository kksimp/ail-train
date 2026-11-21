cart = []
def add(n, q, c):
    for it in cart:
        if it[0] == n: it[1] += q; return
    cart.append([n, q, c])
add("pens", 4, 120); add("paper", 2, 650); add("pens", 8, 120); add("stapler", 1, 899)
tot = lambda: sum(i[1] * i[2] for i in cart)
print(f"before: {tot()} cents, {len(cart)} lines")
s = 0
for it in cart:
    if it[1] >= 10:
        cut = it[2] * 15 // 100; it[2] -= cut; s += cut * it[1]
print(f"bulk discount saved {s} cents")
for it in cart: print(f"  {it[0]:<8} {it[1]:>2} x {it[2]}")
print(f"copy had {len(cart) + 1} lines, cart keeps {len(cart)}")
print(f"after: {tot()} cents")
