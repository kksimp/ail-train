m = lambda c: f"{c // 100}.{c % 100:02}"
def total(items, cents, coupon): return max(sum(cents) - coupon, 0)
q_items, q_cents, q_coupon = ["kettle", "toaster"], [3499, 2999], 0
items, cents, coupon = ["kettle", "toaster", "mug set"], [2999, 2999, 1250], 500
qt = total(q_items, q_cents, q_coupon); ct = total(items, cents, coupon)
print(f"quote: {', '.join(q_items)} = {m(qt)}")
print(f"cart:  {', '.join(items)} = {m(ct)}")
print(f"cart costs {m(ct - qt)} more than quoted")
print(f"staff price would be {m(total(items, cents, coupon + sum(cents) // 10))}")
print(f"cart coupon still {m(coupon)}")
