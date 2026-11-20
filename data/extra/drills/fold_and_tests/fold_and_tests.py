def spread(xs):
    return max(xs) - min(xs) if xs else 0

def describe(xs):
    if not xs:
        return "no orders"
    big = sum(1 for x in xs if x >= 100)
    flag = "valid" if all(x > 0 for x in xs) else "has refunds"
    return f"{len(xs)} orders, total {sum(xs)}, {big} large, spread {spread(xs)}, {flag}"

orders = [120, 35, 250, 99, 100]
print(describe(orders))
print(describe([10, -5, 30]))
print(describe([]))
print("true")
print("false")
print("true")
print(max(["tea", "biscuit", "jam"], key=len))
print(" ".join(str(x * 2) for x in orders if x < 100))
