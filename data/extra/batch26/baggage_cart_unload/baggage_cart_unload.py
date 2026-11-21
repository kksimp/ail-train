checked = [("LX401", 18, False), ("LX402", 23, True), ("LX403", 12, False), ("LX404", 31, False), ("LX405", 9, True)]
cart = [b for b in checked if not b[2]] + [b for b in checked if b[2]]
print(f"cart holds {len(cart)} bags, {sum(b[1] for b in cart)} kg")
n = 1
while cart:
    b = cart.pop()
    heavy = " (heavy tag)" if b[1] > 23 else ""
    flag = "priority " if b[2] else ""
    print(f"{n}. {flag}{b[0]} {b[1]} kg{heavy}")
    n += 1
print("after unloading: nothing on the cart")
